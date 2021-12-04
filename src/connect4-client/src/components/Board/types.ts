export interface Props {
  columns: number;
  rows: number;
  board: Array<Array<number>>;
  onTileClick: (id: number) => void;
}
