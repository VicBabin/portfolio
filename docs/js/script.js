document.addEventListener('DOMContentLoaded', function () {
  const images = document.querySelectorAll('.mosaique');
  const overlay = document.getElementById('overlay');

  images.forEach(function (image) {
      image.addEventListener('click', function () {
          // Afficher l'image en grand
          overlay.style.display = 'block';
          const imageSrc = this.src;
          const largeImage = document.createElement('img');
          largeImage.src = imageSrc;
          largeImage.classList.add('large-image');
          overlay.appendChild(largeImage);

          // Définir la taille maximale de l'image en grand
          const maxWidth = window.innerWidth * 0.8; // 80% de la largeur de la fenêtre
          const maxHeight = window.innerHeight * 0.8; // 80% de la hauteur de la fenêtre

          largeImage.style.maxWidth = maxWidth + 'px';
          largeImage.style.maxHeight = maxHeight + 'px';

          // Fermer l'image en grand en cliquant sur l'image elle-même
            function hideLargeImage() {
                overlay.style.display = 'none';
                const largeImage = document.querySelector('.large-image');
                overlay.removeChild(largeImage);
            };
          
          // Fermer l'image en grand en cliquant dessus
          largeImage.addEventListener('click', function () {
              overlay.style.display = 'none';
              overlay.removeChild(largeImage);
          });
        
          // Fermer l'image en cliquants sur l'overlay
          overlay.addEventListener('click', function (event) {
              overlay.style.display = 'none';
              hideLargeImage();
          });
      });
  });
});

