document.addEventListener('DOMContentLoaded', function () {
    // Example for post like interaction
    const likeButtons = document.querySelectorAll('.like-btn');
    likeButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            button.classList.toggle('liked');
            const likeCount = button.nextElementSibling;
            likeCount.textContent = button.classList.contains('liked')
                ? parseInt(likeCount.textContent) + 1
                : parseInt(likeCount.textContent) - 1;
        });
    });
});
