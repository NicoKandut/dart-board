<script lang="ts">
  import { page } from "$app/stores";
</script>

<nav>
  <a class:active={$page.route.id === "/game"} href="/game">
    <span>👨‍👦‍👦</span>
    <span>Game</span>
  </a>
  <a class:active={$page.route.id === "/board"} href="/board">
    <span>🎯</span>
    <span>Board</span>
  </a>
  <a class:active={$page.route.id === "/stats"} href="/stats">
    <span>📖</span>
    <span>Statistics</span>
  </a>
</nav>

<style>
  nav {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 3rem;
    background-color: var(--color-bg-1);
  }

  a {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding-block: 0.5rem;
    gap: 4px;
    text-decoration: none;
    color: var(--color-text);
    font-size: small;
    transition: all cubic-bezier(0.23, 1, 0.32, 1);
  }

  a.active {
    background-color: var(--color-bg-2);
  }
</style>
