<script context="module" lang="ts">
  const formatter = new Intl.NumberFormat("en-US", {
    notation: "compact",
    compactDisplay: "short",
  });
</script>

<script lang="ts">
  export let name: string;
  export let throws: number;
</script>

<li>
  <div class="img-name">
    <span class="image">👨</span>
    <span class="name">{name}</span>
  </div>
  <div />
  <span>{formatter.format(throws)} throws</span>
  <button>📝</button>
  <button>🚮</button>
</li>

<style>
  li {
    all: unset;
    display: grid;
    grid-template-columns: 8rem 1fr auto auto auto;
    align-items: center;
    padding-inline-end: 1rem;
    background-color: var(--color-bg-1);
    gap: 0.5rem;
  }

  .img-name {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 0.5rem;
    border-radius: 5px;
  }

  button {
    all: unset;
    padding: 0.5rem;
    border-radius: 5px;
    cursor: pointer;
  }
</style>
