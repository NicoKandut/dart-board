<script lang="ts">
  import type { Player } from "$lib/types";

  let game_state = "creating";

  let known_players: Player[] = [
    {
      name: "Fuchs",
    },
    {
      name: "Tippi",
    },
    {
      name: "Samuel",
    },
    {
      name: "Nico",
    },
    {
      name: "Max",
    },
    {
      name: "Lukas",
    },
    {
      name: "Felix",
    },
    {
      name: "Lena",
    },
    {
      name: "Felix",
    },
    {
      name: "Lena",
    },
    {
      name: "Felix",
    },
    {
      name: "Lena",
    },
  ];
  let players: Player[] = [];
</script>

<section>
  {#if game_state === "creating"}
    <h3>Players</h3>

    {#if players.length === 0}
      <div class="hint">No players yet. Pick some below.</div>
    {:else}
      <ul>
        {#each players as player}
          <li
            class="player active"
            on:click={() => (players = players.filter((p) => p !== player))}
          >
            <span>😐</span><span>{player.name}</span>
          </li>
        {/each}
      </ul>
    {/if}

    <button
      disabled={players.length < 1}
      on:click={() => (game_state = "playing")}>Start Game</button
    >

    <h3>Add Known Player</h3>

    <ul>
      {#each known_players as player}
        <li
          class="player"
          on:click={() =>
            !players.includes(player) && (players = [...players, player])}
        >
          <span>😐</span><span>{player.name}</span>
        </li>
      {/each}
    </ul>

    <h3>Add New Player</h3>

    <form>
      <input type="text" placeholder="Name" />
      <input type="text" placeholder="😐" />
      <button>Create</button>
    </form>
  {:else if game_state === "playing"}
    <p>Turn 1</p>
    <h3>{players[0].name}</h3>
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
    max-width: 12rem;
    margin-inline: auto;
  }

  button:disabled {
    background-color: gray;
  }

  form {
    display: flex;
    gap: 0.5rem;
    flex-direction: column;
  }

  input {
    height: 48px;
    padding-inline: 1rem;
    border-radius: 5px;
    background-color: var(--color-bg-1);
    color: var(--color-text);
    border: none;
  }
</style>
