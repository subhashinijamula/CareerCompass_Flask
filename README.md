# CareerCompass – ML-Based Career Recommendation System (Flask)

CareerCompass is a Machine Learning-based career recommendation and skill-gap analysis web application developed using Flask.

The application analyzes student profiles based on academic performance, technical skills, soft skills, and career interests to recommend suitable career paths.

It also provides skill-gap analysis, structured learning roadmaps, and interactive career-specific skill trees to guide students toward their career goals.

## Project Overview

Students often find it difficult to identify suitable career paths and understand which skills they need to develop for their desired professions.

CareerCompass addresses this challenge through a Machine Learning-based classification system that analyzes student profiles and recommends suitable career options.

The Flask application provides an interactive web interface where students can complete assessments, explore career recommendations, identify skill gaps, and follow structured learning roadmaps.

## Key Features

- **Student Assessment:** Collects academic details, technical skills, soft skills, and career interests.
- **ML-Based Career Prediction:** Uses a trained classification model to recommend suitable careers.
- **Ranked Career Recommendations:** Displays multiple career options with prediction scores.
- **Skill-Gap Analysis:** Identifies the difference between existing and required skills.
- **Personalized Learning Roadmap:** Organizes learning into three progressive stages.
- **Interactive Career Skill Tree:** Displays skills, topics, practice activities, and projects.
- **Multiple Career Categories:** Supports eight career paths.
- **Responsive Web Interface:** Provides an interactive user experience using HTML, CSS, and JavaScript.

## Career Categories

The system recommends careers from the following eight categories:

1. Data Analyst
2. Data Scientist
3. Machine Learning Engineer
4. Software Developer
5. Cybersecurity Analyst
6. Cloud Engineer
7. Business Analyst
8. UI/UX Designer

## Input Features

The model uses 21 student profile features.

| Category | Features |
|---|---|
| Academic | Education Level, CGPA |
| Technical Skills | Python, Java, SQL, Statistics, Machine Learning, Data Visualization, Web Development, Cybersecurity, Cloud, Design |
| Soft Skills | Communication, Analytical Thinking, Creativity, Problem Solving |
| Career Interests | Research Interest, Business Interest, Design Interest, Security Interest, Infrastructure Interest |

## Machine Learning Methodology

### Dataset

- Total records: 1,440
- Input features: 21
- Target variable: Career
- Career categories: 8
- Dataset type: Synthetic demonstration dataset

### Algorithms Implemented

The following classification algorithms were trained and compared:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

### Model Training Process

- Train-test split: 80:20
- Random state: 42
- Stratified sampling
- 5-fold cross-validation
- Class balancing using `class_weight="balanced"`
- StandardScaler applied within the Logistic Regression pipeline

### Model Evaluation

The algorithms were evaluated using Accuracy, Macro F1-score, and Cross-validation Macro F1-score.

| Algorithm | Test Accuracy | Test Macro F1 | CV Macro F1 |
|---|---:|---:|---:|
| Logistic Regression | 94.79% | 94.79% | 94.89% |
| Decision Tree | 80.56% | 80.72% | 79.33% |
| Random Forest | 93.40% | 93.39% | 92.39% |

### Best Performing Model

Logistic Regression achieved the highest test Macro F1-score of **94.79%** and was selected as the final classification model.

The trained model is saved using Joblib and reused by the Flask application to generate career recommendations.

## Application Workflow

1. Student visits the CareerCompass home page.
2. Student navigates to the assessment page.
3. Completes the assessment form with academic, technical, soft skill, and interest details.
4. Flask sends the submitted profile to the prediction module.
5. The trained ML model generates career predictions.
6. Ranked career recommendations are displayed.
7. Student selects a career to analyze skill gaps.
8. The application identifies skills that need improvement.
9. Student explores the learning roadmap and career-specific skill tree.

## Skill-Gap Analysis

The application compares the student's current skill level with the required skill level for a selected career.

The skill gap is calculated using:

`Skill Gap = max(0, Required Skill Level - Current Skill Level)`

This helps students identify missing skills and prioritize the areas they need to improve.

## Learning Roadmap

CareerCompass provides a three-stage learning roadmap for each selected career.

### Level 1 – Foundations
- Learn fundamental concepts.
- Understand essential terminology.
- Develop basic technical knowledge.

### Level 2 – Intermediate
- Apply concepts to practical problems.
- Complete mini-projects.
- Improve technical skills through practice.

### Level 3 – Advanced Application
- Explore advanced concepts.
- Build practical applications.
- Complete career-oriented capstone projects.

## Career Skill Tree

The application includes a structured career-specific skill tree.

Each skill contains:
- Skill purpose
- Foundation topics
- Intermediate topics
- Advanced topics
- Practice activities
- Mini-projects
- Capstone projects

The skill tree helps students understand how individual skills are connected and how to progress from beginner to advanced levels.

## Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Backend Framework
- Flask

### Frontend
- HTML5
- CSS3
- JavaScript

### Development Tools
- Visual Studio Code
- Git
- GitHub

## Project Architecture

The application follows a modular architecture.

```text
Student Profile
      |
      v
Flask Web Application
      |
      v
Assessment Form
      |
      v
Prediction Module
      |
      v
Trained ML Model
      |
      v
Career Recommendations
      |
      v
Skill-Gap Analysis
      |
      v
Learning Roadmap
      |
      v
Career Skill Tree
```

## Project Structure

```text
CareerCompass_Flask/
│
├── app.py
│
├── dataset/
│   └── career_dataset.csv
│
├── models/
│   ├── career_model.joblib
│   ├── model_metadata.json
│   └── classification_report.json
│
├── src/
│   ├── __init__.py
│   ├── train_model.py
│   ├── prediction.py
│   └── recommendations.py
│
├── templates/
│   ├── index.html
│   ├── assessment.html
│   ├── prediction.html
│   ├── skill_gap.html
│   └── roadmap.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/CareerCompass-Flask.git
```

### 2. Navigate to the Project Folder

```bash
cd CareerCompass-Flask
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows PowerShell:

```powershell
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Flask Application

```bash
python app.py
```

Open the following URL in your browser:

```text
http://127.0.0.1:5000
```

## Model Training

To train the classification model again, run:

```bash
python -m src.train_model
```

The training module evaluates three classification algorithms and saves the selected model and evaluation reports inside the models directory.

The Flask application loads the saved model for generating career predictions. Retraining is not required when the trained model files are already available.

## Flask Application Routes

| Route | Functionality |
|---|---|
| `/` | Home page |
| `/assessment` | Student assessment form |
| `/prediction` | Career recommendations |
| `/skill-gap/<career>` | Skill-gap analysis |
| `/roadmap/<career>` | Learning roadmap and skill tree |
| `/reset` | Reset assessment session |

## Model Artifacts

| File | Description |
|---|---|
| `career_model.joblib` | Saved trained classification model |
| `model_metadata.json` | Model comparison results and metadata |
| `classification_report.json` | Classification evaluation report |

## Future Enhancements

- Integrate real-world student datasets.
- Improve career recommendations with additional ML techniques.
- Add user authentication and student profile management.
- Integrate job-role and industry-demand insights.
- Recommend external learning resources and courses.
- Add career demand and salary analysis.
- Deploy the application on a cloud platform.

## Limitations

- The dataset is synthetic and intended for demonstration purposes.
- The model has not been validated using representative real-world student data.
- Prediction scores should not be interpreted as guaranteed probabilities of career suitability.
- Skill requirements are predefined within the recommendation logic and may not represent every employer's expectations.

## Conclusion

CareerCompass demonstrates how Machine Learning and Flask can be combined to develop an interactive career recommendation system.

By integrating career prediction, skill-gap analysis, learning roadmaps, and interactive skill trees, the application helps students explore potential career paths and understand the skills required to progress toward their goals.

**Developed using Python, Machine Learning, Scikit-learn, and Flask.**
