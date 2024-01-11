document.addEventListener('DOMContentLoaded', function () {
    var overlay = document.getElementById('overlay');
    var largeImage = new Image();
  
    // Fonction pour afficher l'image en grand
    function showLargeImage(src) {
      console.log("Affichage de l'image en grand");
      largeImage.src = src;
      overlay.appendChild(largeImage);
      overlay.style.display = 'flex';
    }
  
    // Cacher l'image en grand
    function hideLargeImage() {
      console.log("Cacher l'image en grand");
      overlay.style.display = 'none';
      overlay.removeChild(largeImage);
    }
  
    // Événement de clic sur l'overlay pour cacher l'image en grand
    overlay.addEventListener('click', function (event) {
      if (event.target === overlay) {
        console.log("Clic sur l'overlay");
        hideLargeImage();
      }
    });
  
    // Événement de clic sur l'image en grand pour la fermer
    largeImage.addEventListener('click', function () {
      console.log("Clic sur l'image en grand");
      hideLargeImage();
    });
  
    // Événement de clic sur le document pour capturer l'élément cliqué
    document.addEventListener('click', function (event) {
      if (event.target.tagName === 'IMG') {
        console.log("Clic sur une image");
        showLargeImage(event.target.src);
      }
    });
});
  