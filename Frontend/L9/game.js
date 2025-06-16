"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
const Endpoints = {
    ELIXIRS: "Elixirs",
    SPELLS: "Spells",
};
let elixirs = [];
let spells = [];
let validOption = undefined;
const gameContainer = document.getElementById("game");
function fetchData(endpoint) {
    return __awaiter(this, void 0, void 0, function* () {
        const response = yield fetch(`https://wizard-world-api.herokuapp.com/${endpoint}`);
        if (!response.ok) {
            throw new Error(`Error fetching data from ${endpoint}`);
        }
        const data = yield response.json();
        return data;
    });
}
function fetchAllData() {
    return __awaiter(this, void 0, void 0, function* () {
        const [elixirsResponse, spellsResponse] = yield Promise.all([
            fetchData(Endpoints.ELIXIRS),
            fetchData(Endpoints.SPELLS),
        ]);
        elixirs = elixirsResponse.filter((elixir) => elixir.effect);
        spells = spellsResponse.filter((spell) => spell.incantation);
    });
}
function getRandomElements(array, count) {
    const indexes = new Set();
    while (indexes.size < count) {
        const randomIndex = Math.floor(Math.random() * array.length);
        indexes.add(randomIndex);
    }
    return Array.from(indexes).map((index) => array[index]);
}
function generateOptions(randomElements) {
    const [rightOption, ...rest] = randomElements;
    const options = [rightOption, ...rest].sort(() => Math.random() > 0.5 ? 1 : -1);
    return {
        rightOption,
        options,
    };
}
function elixirGame() {
    const { options, rightOption } = generateOptions(getRandomElements(elixirs, 3));
    validOption = rightOption.name;
    console.log(`Cheat Mode: Right answer is ${validOption}`);
    renderOptions(`Which elixir effect is: "${rightOption.effect}"?`, options.map((elixir) => elixir.name));
}
function spellGame() {
    const { options, rightOption } = generateOptions(getRandomElements(spells, 3));
    validOption = rightOption.name;
    console.log(`Cheat Mode: Right answer is ${validOption}`);
    renderOptions(`Which spell incantation is: "${rightOption.incantation}"?`, options.map((spell) => spell.name));
}
function renderOptions(question, answers) {
    const questionElement = document.getElementById("question");
    if (!gameContainer || !questionElement) {
        throw new Error("Game container or question element not found");
    }
    gameContainer.innerHTML = "";
    questionElement.textContent = question;
    answers.forEach((answer) => {
        const option = document.createElement("button");
        option.textContent = answer;
        gameContainer.appendChild(option);
    });
}
// Problem pojawia się, ponieważ event.target jest typu EventTarget, 
// który nie gwarantuje istnienia tagName lub textContent
gameContainer.addEventListener("click", (event) => {
    const target = event.target;
    if (target instanceof HTMLElement && target.tagName === "BUTTON") {
        const selectedOption = target.textContent;
        if (selectedOption === validOption) {
            round();
        }
        else {
            alert("Wrong answer!");
        }
    }
});
function round() {
    const randomGame = Math.random() > 0.5 ? elixirGame : spellGame;
    randomGame();
}
function startGame() {
    return __awaiter(this, void 0, void 0, function* () {
        yield fetchAllData();
        round();
    });
}
startGame();
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiZ2FtZS5qcyIsInNvdXJjZVJvb3QiOiIiLCJzb3VyY2VzIjpbImdhbWUudHMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7OztBQXlCQSxNQUFNLFNBQVMsR0FBRztJQUNkLE9BQU8sRUFBRSxTQUFTO0lBQ2xCLE1BQU0sRUFBRSxRQUFRO0NBQ1gsQ0FBQztBQUlWLElBQUksT0FBTyxHQUFhLEVBQUUsQ0FBQztBQUMzQixJQUFJLE1BQU0sR0FBWSxFQUFFLENBQUM7QUFFekIsSUFBSSxXQUFXLEdBQXVCLFNBQVMsQ0FBQztBQUVoRCxNQUFNLGFBQWEsR0FBRyxRQUFRLENBQUMsY0FBYyxDQUFDLE1BQU0sQ0FBQyxDQUFDO0FBRXRELFNBQWUsU0FBUyxDQUFDLFFBQXNCOztRQUMzQyxNQUFNLFFBQVEsR0FBRyxNQUFNLEtBQUssQ0FDeEIsMENBQTBDLFFBQVEsRUFBRSxDQUN2RCxDQUFDO1FBQ0YsSUFBSSxDQUFDLFFBQVEsQ0FBQyxFQUFFLEVBQUUsQ0FBQztZQUNmLE1BQU0sSUFBSSxLQUFLLENBQUMsNEJBQTRCLFFBQVEsRUFBRSxDQUFDLENBQUM7UUFDNUQsQ0FBQztRQUVELE1BQU0sSUFBSSxHQUFHLE1BQU0sUUFBUSxDQUFDLElBQUksRUFBRSxDQUFDO1FBRW5DLE9BQU8sSUFBSSxDQUFDO0lBQ2hCLENBQUM7Q0FBQTtBQUVELFNBQWUsWUFBWTs7UUFDdkIsTUFBTSxDQUFDLGVBQWUsRUFBRSxjQUFjLENBQUMsR0FBRyxNQUFNLE9BQU8sQ0FBQyxHQUFHLENBQUM7WUFDeEQsU0FBUyxDQUFDLFNBQVMsQ0FBQyxPQUFPLENBQUM7WUFDNUIsU0FBUyxDQUFDLFNBQVMsQ0FBQyxNQUFNLENBQUM7U0FDOUIsQ0FBQyxDQUFDO1FBRUgsT0FBTyxHQUFJLGVBQTRCLENBQUMsTUFBTSxDQUFDLENBQUMsTUFBTSxFQUFFLEVBQUUsQ0FBQyxNQUFNLENBQUMsTUFBTSxDQUFDLENBQUM7UUFDMUUsTUFBTSxHQUFJLGNBQTBCLENBQUMsTUFBTSxDQUFDLENB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