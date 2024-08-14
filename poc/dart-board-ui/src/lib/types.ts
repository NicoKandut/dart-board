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
