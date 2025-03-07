document.addEventListener("DOMContentLoaded", function () {
    const boutonAjouter = document.getElementById("ajouter-entree");
    const listeJournal = document.getElementById("journal");
    
    // Charger les entrées existantes depuis le localStorage
    function chargerJournal() {
        const entrees = JSON.parse(localStorage.getItem("journalTIPE")) || [];
        listeJournal.innerHTML = "";
        entrees.forEach((entree, index) => ajouterEntreeDOM(entree, index));
    }
    
    // Ajouter une entrée au DOM avec un bouton Modifier
    function ajouterEntreeDOM(texte, index) {
        const li = document.createElement("li");
        li.textContent = texte;
        
        const boutonModifier = document.createElement("button");
        boutonModifier.textContent = "Modifier";
        boutonModifier.classList.add("modifier");
        boutonModifier.addEventListener("click", function () {
            modifierEntree(index);
        });
        
        li.appendChild(boutonModifier);
        listeJournal.appendChild(li);
    }
    
    // Ajouter une nouvelle entrée
    boutonAjouter.addEventListener("click", function () {
        const texte = prompt("Ajoutez une nouvelle entrée au journal de bord :");
        if (texte) {
            const entrees = JSON.parse(localStorage.getItem("journalTIPE")) || [];
            entrees.push(texte);
            localStorage.setItem("journalTIPE", JSON.stringify(entrees));
            chargerJournal();
        }
    });
    
    // Modifier une entrée existante
    function modifierEntree(index) {
        const entrees = JSON.parse(localStorage.getItem("journalTIPE")) || [];
        const nouveauTexte = prompt("Modifiez l'entrée :", entrees[index]);
        if (nouveauTexte !== null) {
            entrees[index] = nouveauTexte;
            localStorage.setItem("journalTIPE", JSON.stringify(entrees));
            chargerJournal();
        }
    }
    
    // Charger le journal au démarrage
    chargerJournal();
});
