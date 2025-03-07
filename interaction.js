document.addEventListener("DOMContentLoaded", function () {
    const boutonAjouter = document.getElementById("ajouter-entree");
    const listeJournal = document.getElementById("journal");
    
    // Charger les entrées existantes depuis le localStorage
    function chargerJournal() {
        const entrees = JSON.parse(localStorage.getItem("journalTIPE")) || [];
        listeJournal.innerHTML = "";
        entrees.forEach((entree) => ajouterEntreeDOM(entree));
    }
    
    // Ajouter une entrée au DOM
    function ajouterEntreeDOM(texte) {
        const li = document.createElement("li");
        li.textContent = texte;
        listeJournal.appendChild(li);
    }
    
    // Ajouter une nouvelle entrée
    boutonAjouter.addEventListener("click", function () {
        const texte = prompt("Ajoutez une nouvelle entrée au journal de bord :");
        if (texte) {
            ajouterEntreeDOM(texte);
            enregistrerEntree(texte);
        }
    });
    
    // Enregistrer une entrée dans le localStorage
    function enregistrerEntree(texte) {
        const entrees = JSON.parse(localStorage.getItem("journalTIPE")) || [];
        entrees.push(texte);
        localStorage.setItem("journalTIPE", JSON.stringify(entrees));
    }
    
    // Charger le journal au démarrage
    chargerJournal();
});
