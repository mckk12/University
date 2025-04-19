document.addEventListener("DOMContentLoaded", () => {
    const todoList = document.getElementById("todo-list");
    const addTodoForm = document.getElementById("add-todo-form");
    const todoCount = document.getElementById("count");
    const clearAllButton = document.getElementById("todos-clear");

    const updateCount = () => {
        const remainingTodos = todoList.querySelectorAll(
            ".todo__container:not(.todo__container--completed)"
        ).length;
        todoCount.textContent = remainingTodos;
    };

    const attachTodoListeners = (li) => {
        const moveUpButton = li.querySelector(".move-up");
        const moveDownButton = li.querySelector(".move-down");
        const doneButton = li.querySelector(".todo-button:nth-of-type(3)");
        const removeButton = li.querySelector(".todo-button:nth-of-type(4)");

        if (doneButton) {
            doneButton.addEventListener("click", () => {
                li.classList.toggle("todo__container--completed");
                doneButton.textContent = li.classList.contains(
                    "todo__container--completed"
                )
                    ? "Revert"
                    : "Done";
                updateCount();
            });
        }

        if (moveUpButton) {
            moveUpButton.addEventListener("click", () => {
                const prev = li.previousElementSibling;
                if (prev) todoList.insertBefore(li, prev);
            });
        }

        if (moveDownButton) {
            moveDownButton.addEventListener("click", () => {
                const next = li.nextElementSibling;
                if (next) todoList.insertBefore(next, li);
            });
        }

        if (removeButton) {
            removeButton.addEventListener("click", () => {
                li.remove();
                updateCount();
            });
        }
    };

    const createTodoElement = (name) => {
        const li = document.createElement("li");
        li.className = "todo__container";

        const nameDiv = document.createElement("div");
        nameDiv.className = "todo-element todo-name";
        nameDiv.textContent = name;

        const moveUpButton = document.createElement("button");
        moveUpButton.className = "todo-element todo-button move-up";
        moveUpButton.textContent = "↑";

        const moveDownButton = document.createElement("button");
        moveDownButton.className = "todo-element todo-button move-down";
        moveDownButton.textContent = "↓";

        const doneButton = document.createElement("button");
        doneButton.className = "todo-element todo-button";
        doneButton.textContent = "Done";

        const removeButton = document.createElement("button");
        removeButton.className = "todo-element todo-button";
        removeButton.textContent = "Remove";

        li.append(nameDiv, moveUpButton, moveDownButton, doneButton, removeButton);
        attachTodoListeners(li);
        return li;
    };

    addTodoForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const input = addTodoForm.elements["todo-name"];
        const todoName = input.value.trim();
        if (todoName) {
            const newTodo = createTodoElement(todoName);
            todoList.appendChild(newTodo);
            input.value = "";
            updateCount();
        }
    });

    clearAllButton.addEventListener("click", () => {
        todoList.innerHTML = "";
        updateCount();
    });

    const predefinedList = todoList.querySelectorAll(".todo__container");
    predefinedList.forEach((todo) => {
        attachTodoListeners(todo);
    });

    updateCount();
});