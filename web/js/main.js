const data = [
    { image: "assets/img/example-1", description: "Description 1", caption: "Légende 1" },
    { image: "https://dummyjson.com/image/400x200/008080/ffffff?text=Hello+Peter!&fontSize=16", description: "Description 2", caption: "Légende 2" },
    { image: "https://dummyjson.com/image/400x200?type=webp&text=I+am+a+webp+image", description: "Description 3", caption: "Légende 3" },
    { image: "https://dummyjson.com/image/400x200/008080/ffffff?text=Hello+Peter", description: "Description 4", caption: "Légende 4" },
    { image: "https://dummyjson.com/image/400x200/282828", description: "Description 5", caption: "Légende 5" },
    { image: "https://dummyjson.com/image/400x200?type=webp&text=I+am+a+webp+image", description: "Description 6", caption: "Légende 6" }
];

// Sélection des éléments HTML
const description = document.querySelector(".exPrompt"); // Zone de description
const image = document.getElementById("frontIMG"); // Image affichée en front
const backImage = document.getElementById("backIMG"); // Image affichée en back
const captionFront = document.querySelector(".exAV .exDescription"); // Légende de l'image frontale
const captionBack = document.querySelector(".exAR .exDescription"); // Légende de l'image arrière
const flipper = document.querySelector(".examplePrompt"); // Conteneur qui tourne pour l'effet de flip
const dots = document.querySelectorAll(".dot"); // Sélection de tous les boutons de navigation

let currentIndex = 0; // Index de l'image actuelle
let isFlipped = false; // Variable indiquant l'état de la rotation

function updateContent(index) {
    isFlipped = !isFlipped; // Alterne entre front et back

    // Mise à jour de l’image et de la légende AVANT la rotation
    if (isFlipped) {
        backImage.src = data[index].image; // Change l’image arrière
        captionBack.textContent = data[index].caption; // Change la légende arrière
    } else {
        image.src = data[index].image; // Change l’image frontale
        captionFront.textContent = data[index].caption; // Change la légende frontale
    }

    description.textContent = data[index].description; // Met à jour la description

    // Applique une rotation complète fluide
    if (isFlipped) {
        flipper.style.transform = "rotateY(180deg)";
    } else {
        flipper.style.transform = "rotateY(360deg)";
    }

    // Mise à jour des points de navigation (active/désactive les points)
    dots.forEach(dot => dot.classList.remove("active"));
    dots[index].classList.add("active");
}

// Ajoute les événements de clics sur les boutons de navigation
dots.forEach(dot => {
    dot.addEventListener("click", () => {
        currentIndex = parseInt(dot.dataset.index); // Récupère l'index du bouton cliqué
        updateContent(currentIndex); // Met à jour le contenu
    });
});

// Initialisation au chargement de la page
updateContent(currentIndex);
