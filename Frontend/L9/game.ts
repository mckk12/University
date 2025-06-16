type Elixir = {
    id: string;
    name: string;
    effect: string;
    sideEffects: string;
    characteristics: string;
    time: string;
    difficulty: string;
    ingredients: { id: string; name: string }[];
    inventors: { id: string; firstName: string; lastName: string }[];
    manufacturer: string;
  };
  
type Spell = {
    id: string;
    name: string;
    incantation: string;
    effect: string;
    canBeVerbal: boolean;
    type: string;
    light: string;
    creator: string;
};
  

const Endpoints = {
    ELIXIRS: "Elixirs",
    SPELLS: "Spells",
}as const;

type EndpointType = typeof Endpoints[keyof typeof Endpoints];

let elixirs: Elixir[] = [];
let spells: Spell[] = [];

let validOption: string | undefined = undefined;

const gameContainer = document.getElementById("game");

async function fetchData(endpoint: EndpointType) {
    const response = await fetch(
        `https://wizard-world-api.herokuapp.com/${endpoint}`
    );
    if (!response.ok) {
        throw new Error(`Error fetching data from ${endpoint}`);
    }

    const data = await response.json();

    return data;
}

async function fetchAllData() {
    const [elixirsResponse, spellsResponse] = await Promise.all([
        fetchData(Endpoints.ELIXIRS),
        fetchData(Endpoints.SPELLS),
    ]);

    elixirs = (elixirsResponse as Elixir[]).filter((elixir) => elixir.effect);
    spells = (spellsResponse as Spell[]).filter((spell) => spell.incantation);
}


function getRandomElements<T>(array: T[], count: number): T[] {
    const indexes: Set<number> = new Set();

    while (indexes.size < count) {
        const randomIndex = Math.floor(Math.random() * array.length);
        indexes.add(randomIndex);
    }

    return Array.from(indexes).map((index) => array[index]);
}

function generateOptions<T>(randomElements: T[]): { rightOption: T; options: T[] } {
    const [rightOption, ...rest] = randomElements;

    const options = [rightOption, ...rest].sort(() =>
        Math.random() > 0.5 ? 1 : -1
    );

    return {
        rightOption,
        options,
    };
}

function elixirGame() {
    const { options, rightOption } = generateOptions(
        getRandomElements(elixirs, 3)
    );

    validOption = rightOption.name;

    console.log(`Cheat Mode: Right answer is ${validOption}`);

    renderOptions(
        `Which elixir effect is: "${rightOption.effect}"?`,
        options.map((elixir) => elixir.name)
    );
}

function spellGame() {
    const { options, rightOption } = generateOptions(
        getRandomElements(spells, 3)
    );

    validOption = rightOption.name;

    console.log(`Cheat Mode: Right answer is ${validOption}`);

    renderOptions(
        `Which spell incantation is: "${rightOption.incantation}"?`,
        options.map((spell) => spell.name)
    );
}

function renderOptions(question: string, answers: string[]) {
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
gameContainer!.addEventListener("click", (event) => {
    const target = event.target;

    if (target instanceof HTMLElement && target.tagName === "BUTTON") {
        const selectedOption = target.textContent;

        if (selectedOption === validOption) {
        round();
        } else {
        alert("Wrong answer!");
        }
    }
});

function round() {
    const randomGame = Math.random() > 0.5 ? elixirGame : spellGame;
    randomGame();
}

async function startGame() {
    await fetchAllData();
    round();
}

startGame();
