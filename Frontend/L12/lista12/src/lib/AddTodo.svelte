<script lang="ts">
  import { todos } from '../store/todos';
  let newTodo = '';
  const add = () => {
    if (newTodo.trim()) {
      todos.add(newTodo.trim());
      newTodo = '';
    }
  };
</script>

<form class="add-item__container" on:submit|preventDefault={add}>
  <input bind:value={newTodo} type="text" placeholder="What's on your mind?" class="add-item__element add-item__input" required />
  <button type="submit" class="add-item__element add-item__submit">Add</button>
</form>