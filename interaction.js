document.addEventListener("DOMContentLoaded", function () {
    const boutonSauvegarder = document.getElementById("sauvegarder-texte");
    const zoneTexte = document.getElementById("zone-texte");

    // Charger le texte existant depuis le localStorage
    function chargerTexte() {
        const texteSauvegarde = localStorage.getItem("journalTIPE") || "";
        zoneTexte.value = texteSauvegarde;
    }

    // Sauvegarder le texte dans le localStorage
    boutonSauvegarder.addEventListener("click", function () {
        const texte = zoneTexte.value;
        localStorage.setItem("journalTIPE", texte);
        alert("Texte sauvegardé !");
    });

    // Charger le texte au démarrage
    chargerTexte();
});