const API_URL = "http://localhost:8000";

async function fetchBooks() {
    try {
        const response = await fetch(`${API_URL}/books/`);
        const books = await response.json();
        const container = document.getElementById("books-list");
        container.innerHTML = "";

        books.forEach(book => {
            const div = document.createElement("div");
            div.className = "card";
            div.innerHTML = `
                <strong>${book.title}</strong> par ${book.author} <br>
                ISBN: ${book.isbn} | Statut: ${book.available ? "Disponible" : "Emprunté"}
            `;
            container.appendChild(div);
        });
    } catch (error) {
        console.error("Erreur lors de la récupération des livres:", error);
    }
}

// Charger les livres au démarrage
window.onload = fetchBooks;