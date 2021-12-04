import React from "react";
import Tile from "../Tile/Tile";

import styles from "./Column.module.css";
import { Props } from "./types";

export default class Column extends React.PureComponent<Props> {
  render() {
    const { column, rows, board, onTileClick } = this.props;
    const tiles = [];

    for (let row = rows - 1; row >= 0; row--) {
      const tileId = `${row}:${column}`;
      const tile = board[column][row];
      tiles.push(
        <Tile
          key={tileId}
          id={tileId}
          tile={tile}
          onClick={() => onTileClick(column)}
        />
      );
    }

    return (
      <div aria-label={"column"} className={styles.column}>
        {tiles}
      </div>
    );
  }
}
