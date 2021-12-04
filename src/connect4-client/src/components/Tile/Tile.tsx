import React from "react";
import classNames from "classnames";
import styles from "./Tile.module.css";
import { Props } from "./types";

export default class Tile extends React.PureComponent<Props> {
  render() {
    const { id, tile, onClick = () => {} } = this.props;
    const chipCssClass = classNames(
      styles.chip,
      tile === 1 ? styles.yellow : styles.red
    );

    return (
      <div
        aria-label={"tile"}
        className={styles.tile}
        onClick={() => onClick(id)}
      >
        {tile !== 0 && <div className={chipCssClass} />}
      </div>
    );
  }
}
