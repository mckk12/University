<script lang="ts">
  import { todos } from '../store/todos';
  import type { Todo } from '../store/todos';
  export let todo: Todo;
</script>

<li class="todo__container {todo.completed ? 'todo__container--completed' : ''}">
  <div class="todo-element todo-name">{todo.text}</div>
  <button class="todo-element todo-button move-up" on:click={() => todos.moveUp(todo.id)}>↑</button>
  <button class="todo-element todo-button move-down" on:click={() => todos.moveDown(todo.id)}>↓</button>
  <button class="todo-element todo-button" on:click={() => todos.toggle(todo.id)}>{todo.completed ? 'Revert' : 'Done'}</button>
  <button class="todo-element todo-button" on:click={() => todos.remove(todo.id)}>Remove</button>
</li>