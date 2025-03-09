document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggle-theme");
    const body = document.body;

    // Vérifier si l'utilisateur a déjà une préférence de mode
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "light") {
        body.classList.add("light-mode");
        toggleButton.innerHTML = '<i class="fas fa-moon"></i>'; // Icône lune pour le mode clair
    } else {
        toggleButton.innerHTML = '<i class="fas fa-sun"></i>'; // Icône soleil pour le mode sombre
    }

    // Basculer entre les modes
    toggleButton.addEventListener("click", function () {
        body.classList.toggle("light-mode");
        if (body.classList.contains("light-mode")) {
            localStorage.setItem("theme", "light");
            toggleButton.innerHTML = '<i class="fas fa-moon"></i>'; // Icône lune pour le mode clair
        } else {
            localStorage.setItem("theme", "dark");
            toggleButton.innerHTML = '<i class="fas fa-sun"></i>'; // Icône soleil pour le mode sombre
        }
    });
});