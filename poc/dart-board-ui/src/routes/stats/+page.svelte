<script>
  import PlayerPoint from "$lib/PlayerPoint.svelte";
  import StatPoint from "$lib/StatPoint.svelte";
  import statistics from "$lib/store/statistics";

  let displayAllPlayers = false;

  $: displayedPlayers = displayAllPlayers
    ? $statistics.players
    : $statistics.players.slice(0, 5);

  $: bullsEyes =
    $statistics.overall.scoreCounts["50"] +
    $statistics.overall.scoreCounts["25"];
</script>

<section id="overview">
  <StatPoint value={$statistics.overall.throws} description="darts thrown" />
  <StatPoint value={$statistics.overall.games} description="games played" />
  <StatPoint value={$statistics.players.length} description="players" />
  <StatPoint value={bullsEyes} description="bull's eyes" />
</section>

<section id="players">
  <h2>Players</h2>
  <ul>
    {#each displayedPlayers as [player, stats]}
      <PlayerPoint name={player.name} throws={stats.throws} />
    {/each}
    <button on:click={() => (displayAllPlayers = !displayAllPlayers)}>
      {displayAllPlayers ? "Show less" : "Show all"}
    </button>
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
