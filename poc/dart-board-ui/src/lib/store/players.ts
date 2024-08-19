import type { Player } from "$lib/types";
import { writable } from "svelte/store";

const { subscribe, update } = writable([] as Player[]);

export default {
  subscribe,
  addPlayer: (player: Player) => {
    update((players) => [...players, player]);
  },
  removePlayer: (player: Player) => {
    update((players) => players.filter((p) => p !== player));
  },
};
