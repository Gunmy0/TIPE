document.addEventListener("DOMContentLoaded", function () {
    const boutonSauvegarder = document.getElementById("sauvegarder-texte");
    const zoneTexte = document.getElementById("zone-texte");
    const contenuJournal = document.getElementById("contenu-journal");

    // Charger le texte depuis le localStorage
    function chargerTexte() {
        const texteSauvegarde = localStorage.getItem("journalTIPE") || "";
        contenuJournal.textContent = texteSauvegarde; // Afficher le texte chargé
        zoneTexte.value = texteSauvegarde; // Remplir la zone de texte
    }

    // Sauvegarder le texte dans le localStorage et l'afficher
    boutonSauvegarder.addEventListener("click", function () {
        const texte = zoneTexte.value;
        localStorage.setItem("journalTIPE", texte); // Sauvegarder dans le localStorage
        contenuJournal.textContent = texte; // Afficher le texte sur la page
        alert("Texte sauvegardé et affiché !");
    });

    // Charger le texte au démarrage
    chargerTexte();
});