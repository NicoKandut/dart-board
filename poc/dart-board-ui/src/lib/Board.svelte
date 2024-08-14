<script lang="ts">
  import BoardSvg from "./BoardSvg.svelte";
  import { mmToPercent, type HitPoint } from "./types";

  export let hits: HitPoint[];
</script>

<div class="board">
  <BoardSvg />
  {#each hits as hit}
    {@const percent = mmToPercent(hit)}
    <div class="hit-point" style="left: {percent.x}%; top: {percent.y}%">
      <div class="hit-center" />
    </div>
  {/each}
</div>

<style>
  .board {
    display: flex;
    aspect-ratio: 1/1;
    position: relative;
    flex-grow: 1;
    width: 100%;
  }

  .hit-point {
    position: absolute;
    height: 1rem;
    width: 1rem;
    border-radius: 100px;
    border: 2px white solid;
    transform: translate(-50%, -50%);
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: black;
  }

  .hit-center {
    position: absolute;
    height: 0.5rem;
    width: 0.5rem;
    border-radius: 100px;
    border: 2px solid white;
  }
</style>
