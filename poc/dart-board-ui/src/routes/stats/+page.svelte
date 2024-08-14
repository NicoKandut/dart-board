<script>
  import PlayerPoint from "$lib/PlayerPoint.svelte";
  import StatPoint from "$lib/StatPoint.svelte";

  const players = [
    {
      name: "Fuchs",
      throws: 19821,
    },
    {
      name: "Tippi",
      throws: 1237,
    },
    {
      name: "Samuel",
      throws: 1234,
    },
    {
      name: "Nico",
      throws: 23,
    },
    {
      name: "Max",
      throws: 12,
    },
    {
      name: "Lukas",
      throws: 56,
    },
    {
      name: "Felix",
      throws: 123,
    },
    {
      name: "Lena",
      throws: 123,
    },
    {
      name: "Felix",
      throws: 123,
    },
    {
      name: "Lena",
      throws: 123,
    },
    {
      name: "Felix",
      throws: 123,
    },
    {
      name: "Lena",
      throws: 123,
    },
  ];

  let displayAllPlayers = false;

  $: displayedPlayers = displayAllPlayers ? players : players.slice(0, 5);
</script>

<section id="overview">
  <StatPoint value={19821} description="darts thrown" />
  <StatPoint value={49} description="games played" />
  <StatPoint value={7} description="players" />
  <StatPoint value={271} description="bull's eyes" />
</section>

<section id="players">
  <h2>Players</h2>
  <ul>
    {#each displayedPlayers as player}
      <PlayerPoint name={player.name} throws={player.throws} />
    {/each}
    <button on:click={() => (displayAllPlayers = !displayAllPlayers)}>
      {displayAllPlayers ? "Show less" : "Show all"}
    </button>
  </ul>
</section>

<section id="recent">
  <h2>Recent Games</h2>
  <ul>
    <li>Game 1</li>
    <li>Game 2</li>
    <li>Game 3</li>
  </ul>
</section>

<style>
  #overview {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.5rem;
    padding: 1rem;
  }

  section {
    padding-inline: 1rem;
  }

  ul {
    padding-left: unset;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  button {
    all: unset;
    padding: 0.5rem;
    border-radius: 5px;
    cursor: pointer;
    text-align: center;
  }
</style>
