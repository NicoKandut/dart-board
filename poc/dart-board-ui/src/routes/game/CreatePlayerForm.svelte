<script lang="ts">
  import players from "$lib/store/players";

  let symbol = "";
  let name = "";
</script>

<form>
  <input type="emoji" placeholder="😐" required bind:value={symbol} />
  <input type="text" placeholder="Name" required bind:value={name} />
  <button on:click={() => players.addPlayer({ symbol, name })}>➡</button>
</form>

<style>
  form {
    display: grid;
    grid-template-columns: 48px 1fr auto;
    gap: 0.5rem;
  }

  input {
    height: 48px;
    padding-inline: 1rem;
    border-radius: 5px;
    background-color: var(--color-bg-1);
    color: var(--color-text);
    border: none;
    min-width: 1rem;
  }

  button {
    height: 48px;
    font-size: 18px;
    font-weight: bold;
    background-color: green;
    color: white;
    border: none;
    border-radius: 5px;
    width: 100%;
    min-width: 48px;
    max-width: 12rem;
    margin-inline: auto;
  }

  button:disabled {
    background-color: gray;
  }
</style>
