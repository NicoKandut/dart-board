<script lang="ts">
  import CreatePlayerForm from "./CreatePlayerForm.svelte";

  import players from "$lib/store/players";
  import type { Player } from "$lib/types";

  let game_state = "creating";

  let selectedPlayers: Player[] = [];
</script>

<section>
  {#if game_state === "creating"}
    <h3>Players</h3>

    {#if selectedPlayers.length === 0}
      <div class="hint">No players yet. Pick some below.</div>
    {:else}
      <ul>
        {#each selectedPlayers as player}
          <li
            class="player active"
            on:click={() =>
              (selectedPlayers = selectedPlayers.filter((p) => p !== player))}
          >
            <span>{player.symbol}</span><span>{player.name}</span>
          </li>
        {/each}
      </ul>
    {/if}

    <button
      disabled={selectedPlayers.length < 1}
      on:click={() => (game_state = "playing")}>Start Game</button
    >

    <h3>Add Known Player</h3>

    <ul>
      {#each $players as player}
        <li
          class="player"
          on:click={() =>
            !selectedPlayers.includes(player) &&
            (selectedPlayers = [...selectedPlayers, player])}
        >
          <span>{player.symbol}</span><span>{player.name}</span>
        </li>
      {/each}
    </ul>

    <h3>Add New Player</h3>
    <CreatePlayerForm></CreatePlayerForm>
  {:else if game_state === "playing"}
    <p>Turn 1</p>
    <h3>{selectedPlayers[0].name}</h3>
  {/if}
</section>

<style>
  section {
    display: flex;
    flex-direction: column;
    padding: 1rem;
  }
  ul {
    list-style-type: none;
    padding-left: unset;

    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(4rem, 1fr));
    gap: 0.5rem;
  }

  li {
    padding: 0.5rem;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    gap: 4px;
  }

  .hint {
    columns: span all;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 4rem;
  }

  .player {
    padding: 0.5rem;
    border-radius: 5px;
    background-color: var(--color-bg-1);
    aspect-ratio: 1/1;
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
</style>
