<script lang="ts">
  import AddTodo from './lib/AddTodo.svelte';
  import Header from './lib/Header.svelte';
  import TodoList from './lib/TodoList.svelte';
</script>

<div class="body__wrapper">
  <header class="header__wrapper">
    <h1>Hello, Maciej!</h1>
  </header>
  <main class="main">
    <section>
      <AddTodo />
    </section>
    <section>
      <Header />
      <TodoList />
    </section>
  </main>
</div>