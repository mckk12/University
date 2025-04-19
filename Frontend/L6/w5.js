let library = [];

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
