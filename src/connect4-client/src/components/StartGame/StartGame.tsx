import React, { useState } from "react";
import styles from "./StartGame.module.css";

export const StartGame = ({
  startMultiplayerGame,
  startLocalGame,
  joinGame,
}: any) => {
  const [gameId, setGameId] = useState("");

  const handleChange = (event: any) => {
    setGameId(event.target.value);
  };

  return (
    <div className={styles.box}>
      <h2 className={styles.title}>Connect Four!</h2>
      <div>
        <input className={styles.input} value={gameId} onChange={handleChange}></input>
        <button className ={styles.submitButton} onClick={() => joinGame(gameId)}>Join Existing Game</button>
      </div>
      <div>
        <button className={styles.submitButton} onClick={startLocalGame}>
          Start Local co-op Game
        </button>
      </div>
      <div>
        <button className={styles.submitButton} onClick={startMultiplayerGame}>
          Start Multiplayer Game
        </button>
      </div>
    </div>
  );
};
