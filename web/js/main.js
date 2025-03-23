const data = [
    { image: "assets/img/example/1.jpg", prompt: "Un bâteau à voile dans une mer agitée, au clair de lune", descr: "<i>Clair de lune</i>, par Ivan Aivazovsky (1849)" },
    { image: "assets/img/example/2.jpg", prompt: "Un port dans le brouillard à l'aube, style impressioniste", descr: "<i>Impression, soleil levant</i>, par Claude Monet (1872)" },
    { image: "assets/img/example/3.jpg", prompt: "Paysage montagneux des aples, style impressioniste", descr: "<i>Grand Panorama des Alpes, les Dents du Midi</i>, par Gustave Courbet (1877)" },
    { image: "assets/img/example/4.jpg", prompt: "Paysannes du 19ème ramssant les grains de blé", descr: "<i>Des glaneuses</i>, par Jean-François Millet (1857)" },
    { image: "assets/img/example/5.jpg", prompt: "Estampe japonaise d'une île de pêcheurs, vers 1800", descr: "<i>L'île Tsukada dans la province de Musashi</i>, par Hokusai (1830)" },
    { image: "assets/img/example/6.jpg", prompt: "Voyageur observant le paysage, mer de nuage", descr: "<i>Le Voyageur contemplant une mer de nuages</i>, par Caspar David Friedrich (1818)" }
];
// Sélection des éléments HTML
const examplePrompt = document.querySelector(".exPromptText");
const exampleIMG    = document.getElementById("exampleIMG");
const exampleDescr  = document.querySelector(".exResultText");
// Sélection des points
const dots = document.querySelectorAll(".dot");
// Variable INDEX
let currentIndex = 0 ;

function updateContent(index) {
    // Mise à jour de l'index actuel
    currentIndex = index ;
    // Effet de transition d'image
    exampleIMG.style.filter = 'opacity(0) blur(4px)';
    setTimeout(() => {exampleIMG.src = data[index]['image'];
                      examplePrompt.innerHTML  = data[index]['prompt'];
                      exampleDescr.innerHTML   = data[index]['descr'];
                     }, 250);
    setTimeout(() => {exampleIMG.style.filter = '';}, 350);
    // Mise à jour du point actif
    dots.forEach(dot => dot.classList.remove("active"));
    dots[index].classList.add("active");
}

// Événements de clics sur les boutons de navigation
dots.forEach(dot => {
    dot.addEventListener("click", () => {
        currentIndex = parseInt(dot.dataset.index);
        updateContent(currentIndex);
    });
});
// Initialisation au chargement de la page
examplePrompt.innerHTML  = data[currentIndex]['prompt'];
exampleDescr.innerHTML   = data[currentIndex]['descr'];
updateContent(currentIndex);

// Effet de survol de l'image
exampleIMG.addEventListener('mousemove', (e) => {
    const rect = exampleIMG.getBoundingClientRect();
    // Coordonnées centrales de l'élément
    const centerX = rect.left + rect.width / 2 ;
    // Coordonnées de la souris par rapport à l'élément
    const deltaX = e.clientX - centerX ;
    // Calcul des paramètres d'effet
    const rotate = (deltaX / rect.width) * 20 ;
    const scale  = 1 + Math.abs(deltaX / rect.width) * (1 / 20) ;
    // Rotation et scale de l'élément
    exampleIMG.style.transform = `rotateY(${rotate}deg) scale(${scale})` ;
});
// Effet de survol de l'image (retrait)
exampleIMG.addEventListener('mouseleave', () => {
    exampleIMG.style.transform = 'rotateY(0deg) scale(1)';
});
