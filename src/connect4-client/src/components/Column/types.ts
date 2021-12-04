export interface Props {
  column: number;
  rows: number;
  board: Array<Array<number>>;
  onTileClick: (id: number) => void;
}
