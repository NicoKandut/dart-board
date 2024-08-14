<script context="module" lang="ts">
  const formatter = new Intl.NumberFormat("en-US", {
    notation: "compact",
    compactDisplay: "short",
  });
</script>

<script lang="ts">
  import { onMount } from "svelte";

  export let value: number;
  export let description: string;

  let actualValue = 0;

  const start = new Date().getTime();

  const updateCount = () => {
    const now = new Date().getTime();
    const elapsed = now - start;
    const fraction = Math.min(elapsed / 500, 1);

    actualValue = value * fraction;

    if (value % 1 === 0) {
      actualValue = Math.round(actualValue);
    }

    if (fraction < 1) {
      requestAnimationFrame(updateCount);
    }
  };

  onMount(() => {
    requestAnimationFrame(updateCount);
  });
</script>

<div>
  <span class="value">{formatter.format(actualValue)}</span>
  <span class="description">{description}</span>
</div>

<style>
  div {
    background-color: var(--color-bg-1);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 0.5rem;
    border-radius: 5px;
  }

  .value {
    font-size: 2rem;
    font-weight: bold;
  }
</style>
