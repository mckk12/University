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


const addBooksToLibrary = (books) => {
    books.forEach(book => {
        addBookToLibrary(...book);
    });
};

const books = [
    ["Alice in Wonderland", "Lewis Carroll", 200, true, [1, 2, 3]],
    ["1984", "George Orwell", 300, true, [4, 5]],
    ["The Great Gatsby", "F. Scott Fitzgerald", 150, true, [3, 4]],
    ["To Kill a Mockingbird", "Harper Lee", 250, true, [2, 3]],
    ["The Catcher in the Rye", "J.D. Salinger", 200, true, [1, 2]],
    ["The Hobbit", "J.R.R. Tolkien", 300, true, [4, 5]],
    ["Fahrenheit 451", "Ray Bradbury", 200, true, [3, 4]],
    ["Brave New World", "Aldous Huxley", 250, true, [2, 3]],
    ["The Alchemist", "Paulo Coelho", 200, true, [1, 2]],
    ["The Picture of Dorian Gray", "Oscar Wilde", 300, true, [4, 5]],
  ];
  
  addBooksToLibrary(books);
  console.log(library);