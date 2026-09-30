document.addEventListener('DOMContentLoaded', function () {

    const form = document.querySelector('form');

    if (!form) {
        return;
    }

    const submitButton = form.querySelector('button[type="submit"]');

    form.addEventListener('submit', function () {

        if (submitButton) {
            submitButton.disabled = true;
            submitButton.textContent = 'Making Prediction...';
        }

    });

});