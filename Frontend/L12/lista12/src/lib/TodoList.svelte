<script lang="ts">
  import { todos } from '../store/todos';
  import TodoItem from './TodoItem.svelte';
</script>

<ul class="todos__list">
  {#each $todos as todo (todo.id)}
    <TodoItem {todo} />
  {/each}
</ul>