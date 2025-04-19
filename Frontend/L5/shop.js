/**
 * @typedef {Object} Product
 * @property {number} id - Unique identifier for the product.
 * @property {string} name - Name of the product.
 * @property {number} quantity - Number of items to purchase.
 * @property {Date} purchaseBefore - Date by which the product should be purchased.
 * @property {boolean} purchased - Status indicating if the product has been purchased.
 * @property {number} [pricePerUnit] - Price per unit (only for purchased products).
 */

/** @type {Product[]} */
let shoppingList = [];

/**
 * Adds a new product to the shopping list.
 * @param {string} name - Name of the product.
 * @param {number} quantity - Number of items to purchase.
 * @param {string} purchaseBefore - Date string in the format 'YYYY-MM-DD'.
 */
function addProduct(name, quantity, purchaseBefore) {
    const id = Math.floor(Math.random() * 1000000);
    const product = {
        id,
        name,
        quantity,
        purchaseBefore: new Date(purchaseBefore),
        purchased: false,
    };
    shoppingList.push(product);
}

/**
 * Removes a product from the shopping list by its ID.
 * @param {number} id - ID of the product to remove.
 */
function removeProduct(id) {
    shoppingList = shoppingList.filter(product => product.id !== id);
}

/**
 * edits the name of a product by its ID.
 * @param {number} id - ID of the product to edit.
 * @param {string} newName - New name for the product.
 */
function editProductName(id, newName) {
    const product = shoppingList.find(product => product.id === id);
    if (product) product.name = newName;
}

/**
 * edits the status of a product by its ID.
 * @param {number} id - ID of the product to edit.
 * @param {boolean} newStatus - New status for the product.
 */
function editProductStatus(id, newStatus) {
    const product = shoppingList.find(product => product.id === id);
    if (product) product.purchased = newStatus;
    if (product.pricePerUnit) product.pricePerUnit = undefined; // Reset price if product is marked as not purchased

}

/**
 * edits the quantity of a product by its ID.
 * @param {number} id - ID of the product to edit.
 * @param {number} newQuantity - New quantity for the product.
 */
function editProductQuantity(id, newQuantity) {
    const product = shoppingList.find(product => product.id === id);
    if (product) product.quantity = newQuantity;
}

/**
 * edits the purchase date of a product by its ID.
 * @param {number} id - ID of the product to edit.
 * @param {string} newDate - New purchase date in the format 'YYYY-MM-DD'.
 */
function editProductDate(id, newDate) {
    const product = shoppingList.find(product => product.id === id);
    if (product) product.purchaseBefore = new Date(newDate);
}

/**
 * Moves a product to a new position in the shopping list.
 * @param {number} id - ID of the product to move.
 * @param {number} newIndex - New index for the product.
 */
function moveProduct(id, newIndex) {
    const index = shoppingList.findIndex(product => product.id === id);
    if (index !== -1 && newIndex >= 0 && newIndex < shoppingList.length) {
        const [product] = shoppingList.splice(index, 1);
        shoppingList.splice(newIndex, 0, product);
    }
}

/**
 * Returns a list of products that should be purchased today.
 * @returns {Product[]} - List of products to purchase today.
 */
function getProductsToPurchaseToday() {
    const today = new Date().toDateString();
    return shoppingList.filter(
        product => !product.purchased && product.purchaseBefore.toDateString() === today
    );
}

/**
 * Sets the price for a purchased product.
 * @param {number} id - ID of the product to edit.
 * @param {number} price - Price per unit.
 */
function setProductPrice(id, price) {
    const product = shoppingList.find(product => product.id === id);
    if (product && product.purchased) {
        product.pricePerUnit = price;
    }
}

/**
 * Calculates the total cost of purchases for a given day.
 * @param {string} date - Date string in the format 'YYYY-MM-DD'.
 * @returns {number} - Total cost of purchases for the day.
 */
function calculateTotalCost(date) {
    const targetDate = new Date(date).toDateString();
    const products = shoppingList.filter(p => p.purchaseBefore.toDateString() === targetDate && p.purchased);
    return products.reduce((total, product) => {
        return total + (product.pricePerUnit || 0) * product.quantity;
    }, 0);
}

/**
 * Applies a modification function to a list of products by their IDs.
 * @param {number[]} ids - List of product IDs to modify.
 * @param {(product: Product) => Product} func - Function to apply to each product.
 */
function applyFuncToProducts(ids, func) {
    shoppingList.forEach(product => {
        if (ids.includes(product.id)) {
            func(product);
        }
    });
}

addProduct("Milk", 2, "2023-12-01");
addProduct("Bread", 1, "2023-12-01");
addProduct("Eggs", 12, "2023-12-02");
console.log("Initial shopping list:", shoppingList);

removeProduct(shoppingList[0].id); 
editProductName(shoppingList[0].id, "Whole Grain Bread");
editProductStatus(shoppingList[0].id, true);
editProductQuantity(shoppingList[1].id, 6);
editProductDate(shoppingList[1].id, "2023-12-03");
moveProduct(shoppingList[1].id, 0); 

const productsToPurchaseToday = getProductsToPurchaseToday();
console.log("Products to purchase today:", productsToPurchaseToday);

setProductPrice(shoppingList[0].id, 2.5); 

const totalCost = calculateTotalCost("2023-12-01");
console.log("Total cost for 2023-12-01:", totalCost);

applyFuncToProducts(
    [shoppingList[0].id, shoppingList[1].id],
    product => (product.quantity += 1) 
);
console.log("Updated shopping list:", shoppingList);
