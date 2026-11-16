
document.addEventListener("DOMContentLoaded", function () {

    const branchButtons = document.querySelectorAll(
        ".skill-branch-header"
    );

    branchButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const branch = button.closest(".skill-branch");

            const isOpen = branch.classList.toggle("is-open");

            button.setAttribute(
                "aria-expanded",
                isOpen ? "true" : "false"
            );

        });

    });

});
