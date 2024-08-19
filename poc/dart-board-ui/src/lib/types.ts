export interface HitPoint {
  x: number;
  y: number;
  score: number;
}

export interface Point {
  x: number;
  y: number;
}

export const mmToPercent = (point: HitPoint): Point => ({
  x: ((point.x + 170) / 340) * 100,
  y: ((-point.y + 170) / 340) * 100,
});

export interface Player {
  symbol: string;
  name: string;
}

export interface ScoreMap {
  [key: string]: number;
}

export interface PlayerStatistics {
  throws: number;
  score_map: ScoreMap;
}

export interface Score {
  base: number;
  modifier: number;
}

export type ScoreNumber = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20;
export type ScoreString = 0 | `${ScoreNumber}` | `D${ScoreNumber}` | `T${ScoreNumber}`;

export const scoreToString = (score: Score): string => {
  if (score.modifier === 1) {
    return `D${score.base}`;
  } else if (score.modifier === 2) {
    return `T${score.base}`;
  } else {
    return `${score.base}`;
  }
};

export const parseScore = (score: string): Score => {
  if (score.startsWith("D")) {
    return {
      base: parseInt(score.slice(1)),
      modifier: 1,
    };
  } else if (score.startsWith("T")) {
    return {
      base: parseInt(score.slice(1)),
      modifier: 2,
    };
  } else {
    return {
      base: parseInt(score),
      modifier: 0,
    };
  }
};
