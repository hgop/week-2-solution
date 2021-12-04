import React, { useState } from "react";
import OnlineMultiplayerGame from "../OnlineMultiplayerGame/OnlineMultiplayerGame";
import LocalCoopGame from "../LocalCoopGame/LocalCoopGame";
import { StartGame } from "../StartGame/StartGame";

import {
  Game,
  GameApiClient,
  MockGameClient,
} from "../../external_services/game_api_client";

interface AppProps {
  columns: number;
  rows: number;
  client: GameApiClient | MockGameClient;
}

interface OnlineMultiplayer {
  type: "OnlineMultiplayer",
  game: Game
}

interface LocalCoop {
  type: "LocalCoop",
  playerOne: Game,
  playerTwo: Game
}

interface None {
  type: "None"
}

type GameType =
  | OnlineMultiplayer
  | LocalCoop
  | None;

export const App = ({ columns, rows, client }: AppProps) => {
  const [gameType, setGameType] = useState<GameType>({ type: "None" });

  const handleMultiplayerGameStart = () => {
    client.createGame({}).then((game: Game) => {
      setGameType({
        type: "OnlineMultiplayer",
        game: game
      });
    });
  };

  const handleLocalGameStart = () => {
    client.createGame({}).then((player_one_game: Game) => {
      client.joinGame({ gameId: player_one_game.gameId }).then((player_two_game: Game) => {
        setGameType({
          type: "LocalCoop",
          playerOne: player_one_game,
          playerTwo: player_two_game
        });
      });
    });
  };

  const handleJoinGame = (gameId: string) => {
    client.joinGame({ gameId: gameId }).then((game: Game) => {
      setGameType({
        type: "OnlineMultiplayer",
        game: game
      });
    });
  };

  switch (gameType.type) {
    case "OnlineMultiplayer":
      return <OnlineMultiplayerGame
        initialGame={gameType.game}
        columns={columns}
        rows={rows}
        client={client}
        handlePlayAgain={() => setGameType({ type: "None" })}
      />;
    case "LocalCoop":
      return <LocalCoopGame
        initialGame={gameType.playerOne}
        playerOneId={gameType.playerOne.playerId}
        playerTwoId={gameType.playerTwo.playerId}
        columns={columns}
        rows={rows}
        client={client}
        handlePlayAgain={() => setGameType({ type: "None" })}
      />;
    case "None":
      return <StartGame
        startLocalGame={() => handleLocalGameStart()}
        startMultiplayerGame={() => handleMultiplayerGameStart()}
        joinGame={(value: any) => handleJoinGame(value)}
      />;
  }
};

export default App;
