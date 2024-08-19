<script lang="ts">
  import "../app.css";
  import Navigation from "../lib/Navigation.svelte";
</script>

<div class="app">
  <main>
    <slot />
  </main>

  <footer>
    <Navigation />
  </footer>
</div>

<style>
  .app {
    background-color: var(--color-bg-0);
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
  }

  main {
    flex-grow: 1;
    overflow-y: scroll;
  }
</style>
