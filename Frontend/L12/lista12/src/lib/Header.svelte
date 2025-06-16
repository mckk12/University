<script lang="ts">
  import { todos } from '../store/todos';
  $: count = $todos.filter(t => !t.completed).length;
</script>

<header class="todos-header__container">
  <h2>
    Todo List (<span>{count}</span> remaining)
    <button class="todos-clear" on:click={() => todos.clear()}>Clear all</button>
  </h2>
</header>