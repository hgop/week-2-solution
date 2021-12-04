import React, { useState } from "react";
import Board from "../Board/Board";
import styles from "./LocalCoopGame.module.css";

import {
  Game,
  GameApiClient,
  Player,
  Tile,
} from "../../external_services/game_api_client";

interface Props {
  columns: number;
  rows: number;
  client: GameApiClient;
  initialGame: Game;
  playerOneId: string;
  playerTwoId: string;
  handlePlayAgain: () => void;
}

interface GameState {
  gameId: string;
  active: boolean;
  winner?: string;
  activePlayer: Player;
  board: Array<Array<Tile>>;
}

const LocalCoopGame = ({
  columns,
  rows,
  client,
  initialGame,
  playerOneId,
  playerTwoId,
  handlePlayAgain,
}: Props) => {

  const [gameState, setGameState] = useState<GameState>({
    gameId: initialGame.gameId,
    active: initialGame.active,
    winner: initialGame.winner,
    activePlayer: initialGame.activePlayer,
    board: initialGame.board,
  });

  const handleMakeMove = (column: number) => {
    client
      .makeMove({
        gameId: gameState.gameId,
        playerId: gameState.activePlayer === Player.One ? playerOneId : playerTwoId,
        column: column,
      })
      .then((game?: Game) => {
        if (game === undefined) return;
        setGameState({
          gameId: game.gameId,
          active: game.active,
          winner: game.winner,
          activePlayer: game.activePlayer,
          board: game.board,
        });
      });
  };

  return (
    <div className={styles.app}>
      <h2>This is a Local Coop Game</h2>
      {
        gameState.winner ?
          <><h3>Player {gameState.winner}!!</h3>
            <h2> &#128020; &#127881; &#128020; WINNER WINNER CHICKEN DINNER!!! &#128020; &#127881; &#127881;  </h2></> :
          <h3>{`It\'s Player\'s ${gameState.activePlayer} turn`}</h3>
      }
      <Board
        columns={columns}
        rows={rows}
        board={gameState.board}
        onTileClick={(id) => {
          handleMakeMove(id);
        }}
      />
      {gameState.active ? null : (
        <button style={{ width: "100%" }} onClick={handlePlayAgain}>
          Play Again
        </button>
      )}
    </div>
  );
};

export default LocalCoopGame;
