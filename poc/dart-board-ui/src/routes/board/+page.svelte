<script lang="ts">
  import { onDestroy, onMount } from "svelte";
  import Board from "../../lib/Board.svelte";
  import type { HitPoint } from "../../lib/types.ts";

  const randomCoordinate = () => (Math.random() * 2 - 1) * 170;

  let hits: HitPoint[] = [];
  let interval: number;

  onMount(() => {
    interval = setInterval(() => {
      if (hits.length === 3) {
        hits = [];
      } else {
        hits = [
          ...hits,
          {
            x: randomCoordinate(),
            y: randomCoordinate(),
            score: Math.random() * 60,
          },
        ];
      }
    }, 500);
  });

  onDestroy(() => {
    clearInterval(interval);
  });
</script>

<Board {hits} />

<ol>
  {#each hits as hit, i}
    <li class:active={i + 1 === hits.length}>
      <small>Throw {i + 1}</small>
      <span>🎯 {Math.round(hit.score)} pts</span>
    </li>
  {/each}

  {#each { length: 3 - hits.length } as _, i}
    <li>
      <small>Throw {i + 1}</small>
      <span>❔</span>
    </li>
  {/each}
</ol>

<div class="controls">
  <button>🔙 Undo</button>
  <button>📝 Edit</button>
  <button>⏩ Skip</button>
</div>

<style>
  ol {
    all: unset;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    flex-direction: row;
    gap: 2px;
    width: 100%;
  }

  li {
    background-color: #ffffff12;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1rem;
    gap: 0.25rem;
    border-radius: 3px;
    font-weight: bold;
  }

  li.active {
    background-color: #ffffff24;
  }

  small {
    font-weight: normal;
  }

  .controls {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    flex-direction: row;
    gap: 2px;
    width: 100%;
  }

  .controls button {
    border-radius: 3px;
    border: unset;
    min-height: 48px;
  }

  .controls button:nth-child(1) {
    background-color: #e22d26;
  }

  .controls button:nth-child(2) {
    background-color: rgb(147, 52, 139);
  }

  .controls button:nth-child(3) {
    background-color: #349334;
  }
</style>
