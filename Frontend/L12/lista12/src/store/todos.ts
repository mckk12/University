import { writable } from 'svelte/store';

export interface Todo {
    id: number;
    text: string;
    completed: boolean;
}

function createTodoStore() {
    const { subscribe, update, set } = writable<Todo[]>([]);

    interface TodoStore {
        subscribe: typeof subscribe;
        add: (text: string) => void;
        remove: (id: number) => void;
        toggle: (id: number) => void;
        clear: () => void;
        moveUp: (id: number) => void;
        moveDown: (id: number) => void;
    }

    return {
        subscribe,
        add: (text: string): void => update((todos: Todo[]) => [...todos, { id: Date.now(), text, completed: false }]),
        remove: (id: number): void => update((todos: Todo[]) => todos.filter(todo => todo.id !== id)),
        toggle: (id: number): void => update((todos: Todo[]) => todos.map(todo => todo.id === id ? { ...todo, completed: !todo.completed } : todo)),
        clear: (): void => set([]),
        moveUp: (id: number): void => update((todos: Todo[]) => {
            const idx = todos.findIndex(todo => todo.id === id);
            if (idx > 0) {
                const newTodos = [...todos];
                [newTodos[idx - 1], newTodos[idx]] = [newTodos[idx], newTodos[idx - 1]];
                return newTodos;
            }
            return todos;
        }),
        moveDown: (id: number): void => update((todos: Todo[]) => {
            const idx = todos.findIndex(todo => todo.id === id);
            if (idx >= 0 && idx < todos.length - 1) {
                const newTodos = [...todos];
                [newTodos[idx + 1], newTodos[idx]] = [newTodos[idx], newTodos[idx + 1]];
                return newTodos;
            }
            return todos;
        })
    } as TodoStore;
}

export const todos = createTodoStore();