document.addEventListener('DOMContentLoaded', (event) => {
    const likeButton = document.getElementById('like-button');
    const likeCount = document.getElementById('like-count');
    
    // contador de likes inicial (podría venir de una base de datos)
    let likes = 0;

    likeButton.addEventListener('click', () => {
        likes++;
        likeCount.textContent = likes;
    });
});
