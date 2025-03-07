document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggle-theme");
    const body = document.body;

    // Vérifier si l'utilisateur a déjà une préférence de mode
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "light") {
        body.classList.add("light-mode");
        toggleButton.textContent = "Mode Sombre";
    }

    // Basculer entre les modes
    toggleButton.addEventListener("click", function () {
        body.classList.toggle("light-mode");
        if (body.classList.contains("light-mode")) {
            localStorage.setItem("theme", "light");
            toggleButton.textContent = "Mode Sombre";
        } else {
            localStorage.setItem("theme", "dark");
            toggleButton.textContent = "Mode Clair";
        }
    });
});