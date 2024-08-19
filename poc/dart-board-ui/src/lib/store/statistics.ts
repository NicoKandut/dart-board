import type { Player, PlayerStatistics, ScoreMap } from "$lib/types";
import { writable } from "svelte/store";

export default writable({
  overall: {
    throws: 0,
    games: 0,
    scoreCounts: {} as ScoreMap,
  },
  players: [] as Array<[Player, PlayerStatistics]>,
});
