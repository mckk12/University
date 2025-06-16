document.addEventListener("DOMContentLoaded", async () => {
    const pokemonListElement = document.getElementById("pokemonList");
    const loadingElement = document.getElementById("loading");
    const errorTextElement = document.getElementById("errorText");
    const pokemonDetailsElement = document.getElementById("pokemonDetails");
    const pokemonNameElement = document.getElementById("pokemonName");
    const pokemonImgElement = document.getElementById("pokemonImg");
    const pokemonTypesElement = document.getElementById("pokemonTypes");
    const pokemonStatsElement = document.getElementById("pokemonStats");
    const pokemonFlavorTextElement = document.getElementById("pokemonFlavorText");

    const API_BASE = "https://pokeapi.co/api/v2";
    const POKEMON_COUNT = 151;

    async function fetchPokemons() {
        const response = await fetch(`${API_BASE}/pokemon?limit=${POKEMON_COUNT}`);
        if (!response.ok) throw new Error("Failed to fetch Pokémon list");
        const data = await response.json();
        return data.results
    }

    function showPokemonList(pokemonList) {
        pokemonListElement.innerHTML = "";
        pokemonList.forEach((pokemon, index) => {
            const listItem = document.createElement("li");
            listItem.textContent = pokemon.name;
            listItem.addEventListener("click", () => showPokemonDetails(index+1));
            pokemonListElement.appendChild(listItem);
    });
    }

    async function showPokemon(pokemonId){
        pokemonDetailsElement.style.display = "none";
    
        const speciesResponse = await fetch(`${API_BASE}/pokemon-species/${pokemonId}`);
        if (!speciesResponse.ok) throw new Error("Failed to fetch Pokémon species");
        const speciesData = await speciesResponse.json();

        const defaultVariety = speciesData.varieties.find(v => v.is_default);
        const pokemonResponse = await fetch(defaultVariety.pokemon.url);
        if (!pokemonResponse.ok) throw new Error("Failed to fetch Pokémon data");
        const pokemonData = await pokemonResponse.json();

        const flavorText = speciesData.flavor_text_entries.find(entry => entry.language.name === "en")?.flavor_text.replace(/[\n\f]/g, " ") || "No description available.";

        await preloadImage(pokemonData.sprites.front_default);

        pokemonNameElement.textContent = pokemonData.name;
        pokemonImgElement.src = pokemonData.sprites.front_default;
        pokemonImgElement.alt = pokemonData.name;

        pokemonTypesElement.innerHTML = "";
        pokemonData.types.forEach(type => {
            const typeSpan = document.createElement("span");
            typeSpan.className = "type";
            typeSpan.textContent = type.type.name;
            pokemonTypesElement.appendChild(typeSpan);
        });

        pokemonStatsElement.innerHTML = "";
        pokemonData.stats.forEach(stat => {
            const statDiv = document.createElement("div");
            statDiv.className = "stat";
            statDiv.innerHTML = `<span>${stat.stat.name}</span><span>${stat.base_stat}</span>`;
            pokemonStatsElement.appendChild(statDiv);
        });

        pokemonFlavorTextElement.textContent = flavorText;

        pokemonDetailsElement.style.display = "flex";
    }

    async function showPokemonDetails(pokemonId) {
        try {
            showLoading();
            await showPokemon(pokemonId);
        } catch (error) {
            showError();
        } finally {
            hideLoading();
        }
    }
        
    async function preloadImage(src) {
        const img = new Image();
        img.src = src;
        await img.decode();
        return img;
    }

    function showLoading() {
        loadingElement.style.display = "block";
        errorTextElement.style.display = "none";
    }
    
    function hideLoading() {
        loadingElement.style.display = "none";
    }
    
    function showError() {
        errorTextElement.style.display = "block";
        pokemonDetailsElement.style.display = "none";
    }

    try {
        showLoading();
        const pokemonList = await fetchPokemons();
        showPokemonList(pokemonList);
    } catch (error) {
        showError();
    } finally {
        hideLoading();
    }
})
