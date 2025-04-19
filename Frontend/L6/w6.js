const testCases = [
    { testCase: ["", "Author", 200, true, []], shouldFail: true },
    { testCase: ["Title", "", 200, true, []], shouldFail: true },
    { testCase: ["Title", "Author", -1, true, []], shouldFail: true },
    { testCase: ["Title", "Author", 200, "yes", []], shouldFail: true },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3, 6]], shouldFail: true },
    {
      testCase: ["Title", "Author", 200, true, [1, 2, 3, "yes"]],
      shouldFail: true,
    },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3, {}]], shouldFail: true },
    { testCase: ["Title", "Author", 200, true, []], shouldFail: false },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3]], shouldFail: false },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3, 4]], shouldFail: false },
    {
      testCase: ["Title", "Author", 200, true, [1, 2, 3, 4, 5]],
      shouldFail: false,
    },
    {
      testCase: ["Title", "Author", 200, true, [1, 2, 3, 4, 5]],
      shouldFail: false,
    },
];

library = [];
const addBookToLibrary = (title, author, pages, isAvailable, ratings) => {
    if (
        title.trim() === "" || typeof title !== "string" ||
        author.trim() === "" || typeof author !== "string" ||
        pages <= 0 || typeof pages !== "number" ||
        typeof isAvailable !== "boolean" || 
        !Array.isArray(ratings) || 
        ratings.some(rating => typeof rating !== "number" || rating < 0 || rating > 5)
    ) {
        throw new Error("Invalid input");
    }

    library.push({
        title,
        author,
        pages,
        available: isAvailable,
        ratings,
    });
};


const testAddBookToLibrary = () => {
    testCases.forEach(({ testCase, shouldFail }) => {
        try {
            addBookToLibrary(...testCase);
            if (shouldFail) {
                console.log(`Test failed for input: ${JSON.stringify(testCase)}`);
            } else {
                console.log(`Test passed for input: ${JSON.stringify(testCase)}`);
            }
        } catch (error) {
            if (shouldFail) {
                console.log(`Test passed for input: ${JSON.stringify(testCase)}`);
                console.error(`Error: ${error.message}`);
            } else {
                console.log(`Test failed for input: ${JSON.stringify(testCase)}`);
                console.error(`Error: ${error.message}`);
            }
        }
    });
}
testAddBookToLibrary();