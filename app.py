
from flask import Flask, render_template, request, session, redirect, url_for

from src.prediction import predict_profile

from src.recommendations import (
    get_skill_gaps,
    get_roadmap,
    get_career_skill_tree
)


# ==========================================================
# FLASK APPLICATION CONFIGURATION
# ==========================================================

app = Flask(__name__)

app.secret_key = "careercompass_secret_key"


# ==========================================================
# HOME PAGE
# ==========================================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================================
# CAREER ASSESSMENT
# ==========================================================

@app.route("/assessment", methods=["GET", "POST"])
def assessment():

    if request.method == "POST":

        try:

            # Get assessment form data
            form_data = request.form.to_dict()

            # Convert form values into numbers
            profile = {
                key: float(value)
                for key, value in form_data.items()
            }

            # Save user profile in session
            session["profile"] = profile

            # Generate career predictions only once
            predictions = predict_profile(profile)

            if not predictions:

                return "No career predictions were generated."

            # Ensure prediction values are session-serializable
            predictions = [
                {
                    "career": str(item["career"]),
                    "score": float(item["score"])
                }
                for item in predictions
            ]

            # Save predictions in session
            session["predictions"] = predictions

            # Display prediction page
            return render_template(
                "prediction.html",
                predictions=predictions
            )

        except Exception as e:

            app.logger.exception("Assessment failed")

            return (
                f"Unable to generate prediction: {str(e)}",
                500
            )

    return render_template("assessment.html")


# ==========================================================
# CAREER RECOMMENDATIONS
# ==========================================================

@app.route("/prediction")
def prediction():

    # Retrieve previously generated predictions
    predictions = session.get("predictions")

    # If no predictions exist, redirect to assessment
    if not predictions:

        return redirect(url_for("assessment"))

    # Display saved predictions without running the model again
    return render_template(
        "prediction.html",
        predictions=predictions
    )


# ==========================================================
# SKILL GAP ANALYSIS
# ==========================================================

@app.route("/skill-gap/<career>")
def skill_gap(career):

    # Retrieve saved assessment profile
    profile = session.get("profile")

    if not profile:

        return redirect(url_for("assessment"))

    try:

        # Calculate skill gaps for selected career
        skill_gaps = get_skill_gaps(
            career,
            profile
        )

        return render_template(
            "skill_gap.html",
            career=career,
            skill_gaps=skill_gaps
        )

    except ValueError:

        return "Invalid career selected.", 404

    except Exception as e:

        app.logger.exception("Skill gap analysis failed")

        return (
            f"Unable to generate skill gap analysis: {str(e)}",
            500
        )


# ==========================================================
# CAREER LEARNING ROADMAP
# ==========================================================

@app.route("/roadmap/<career>")
def roadmap(career):

    # Retrieve saved assessment profile
    profile = session.get("profile")

    if not profile:

        return redirect(url_for("assessment"))

    try:

        # Calculate skill gaps
        skill_gaps = get_skill_gaps(
            career,
            profile
        )

        # Generate three-stage roadmap
        roadmap_stages = get_roadmap(
            career,
            skill_gaps
        )

        # Retrieve detailed career skill tree
        skill_tree = get_career_skill_tree(career)

        return render_template(
            "roadmap.html",
            career=career,
            skill_gaps=skill_gaps,
            roadmap_stages=roadmap_stages,
            skill_tree=skill_tree
        )

    except ValueError:

        return "No roadmap found for this career.", 404

    except Exception as e:

        app.logger.exception("Roadmap generation failed")

        return (
            f"Unable to generate roadmap: {str(e)}",
            500
        )


# ==========================================================
# RESET APPLICATION
# ==========================================================

@app.route("/reset")
def reset():

    # Clear saved profile and predictions
    session.clear()

    return redirect(url_for("home"))


# ==========================================================
# RUN FLASK APPLICATION
# ==========================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )
