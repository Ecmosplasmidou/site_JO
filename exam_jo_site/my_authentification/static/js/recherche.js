const searchInput = document.getElementById('search');
const searchResult = document.getElementById('suggestions');

async function getUser() {
    const response = await fetch('/search/?recherche=' + searchInput.value);
    const data = await response.json();
    const orderedData = orderList(data.results);
    console.log(orderedData);
    displayResults(orderedData);
}

searchInput.addEventListener('input', () => {
    if (searchInput.value.length > 2) { // Commencer à chercher après 3 caractères
        getUser();
    } else {
        searchResult.innerHTML = ''; // Vider les résultats précédents si la longueur est <= 2
    }
});

function orderList(data) {
    return data.sort((a, b) => a.localeCompare(b));
}

function displayResults(results) {
    searchResult.innerHTML = ''; // Vider les résultats précédents
    results.forEach(item => {
        const div = document.createElement('div');
        div.textContent = item;
        div.classList.add('suggestion-item'); // Ajouter une classe pour styliser les suggestions
        searchResult.appendChild(div);
    });
}