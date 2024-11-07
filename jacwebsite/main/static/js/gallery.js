// Sélectionner tous les éléments vidéo dans la galerie
const videos = document.querySelectorAll('.gallery-item video');

videos.forEach(video => {
    // Activer le son lorsque la souris passe sur la vidéo
    video.addEventListener('mouseenter', () => {
        video.muted = false; // Désactiver le mode muet
    });

    // Remettre le son en mode muet lorsque la souris quitte la vidéo
    video.addEventListener('mouseleave', () => {
        video.muted = true; // Réactiver le mode muet
    });
});