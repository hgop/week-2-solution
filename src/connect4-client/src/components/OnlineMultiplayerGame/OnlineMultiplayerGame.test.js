import React from 'react';
import ReactDOM from 'react-dom';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import OnlineMultiplayerGame from './OnlineMultiplayerGame';
import {
    MockGameClient,
    GameApiClient
} from "../../external_services/game_api_client";



var mockGame = null;
var gameClient = null;

beforeEach(async () => {
    gameClient = new MockGameClient();

    await gameClient.createGame().then((data) => {
        mockGame = data;
    });
});

it('should render without crashing', () => {
    const div = document.createElement('div');
    ReactDOM.render(<OnlineMultiplayerGame
        columns={4}
        rows={4}
        client={GameApiClient}
        initialGame={mockGame}
        handlePlayAgain={(_) => { }}
    />, div);
});

it('should render basic texts', () => {

    render(<OnlineMultiplayerGame
        columns={4}
        rows={4}
        client={GameApiClient}
        initialGame={mockGame}
        handlePlayAgain={(_) => { }}
    />);
    expect(screen.getByText("You are player: 1")).toBeInTheDocument();
    expect(screen.getByText("Game Id: JFKS343HD")).toBeInTheDocument();
    expect(screen.getByText(`It's Player ${mockGame.activePlayer}'s turn`)).toBeInTheDocument();
    expect(screen.getByText("You are player: 1")).toBeInTheDocument();
});

it('should render "Waiting for more players" texts', () => {

    mockGame.playerCount = 1;

    render(<OnlineMultiplayerGame
        columns={4}
        rows={4}
        client={GameApiClient}
        initialGame={mockGame}
        handlePlayAgain={(_) => { }}
    />);
    expect(screen.getByText("Waiting for more players")).toBeInTheDocument();
});

it('should render player 1 turn texts', () => {

    mockGame.activePlayer = 1;

    render(<OnlineMultiplayerGame
        columns={4}
        rows={4}
        client={GameApiClient}
        initialGame={mockGame}
        handlePlayAgain={(_) => { }}
    />);
    expect(screen.getByText(`It's Player 1's turn`)).toBeInTheDocument();
});

it('should render player 2 turn texts', () => {

    mockGame.activePlayer = 2;

    render(<OnlineMultiplayerGame
        columns={4}
        rows={4}
        client={GameApiClient}
        initialGame={mockGame}
        handlePlayAgain={(_) => { }}
    />);
    expect(screen.getByText(`It's Player 2's turn`)).toBeInTheDocument();
});

it('should render player 1 won texts', () => {

    mockGame.winner = 1;

    render(<OnlineMultiplayerGame
        columns={4}
        rows={4}
        client={GameApiClient}
        initialGame={mockGame}
        handlePlayAgain={(_) => { }}
    />);
    expect(screen.getByText(`WINNER WINNER CHICKEN DINNER, Player 1 won the game`)).toBeInTheDocument();
});

it('should render player 2 won texts', () => {

    mockGame.winner = 2;

    render(<OnlineMultiplayerGame
        columns={4}
        rows={4}
        client={GameApiClient}
        initialGame={mockGame}
        handlePlayAgain={(_) => { }}
    />);
    expect(screen.getByText(`WINNER WINNER CHICKEN DINNER, Player 2 won the game`)).toBeInTheDocument();
});

it('should render draw texts', () => {

    mockGame.active = false;

    render(<OnlineMultiplayerGame
        columns={4}
        rows={4}
        client={GameApiClient}
        initialGame={mockGame}
        handlePlayAgain={(_) => { }}
    />);
    expect(screen.getByText(`Game finished with a draw`)).toBeInTheDocument();
    expect(screen.getByText(`Play Again`)).toBeInTheDocument();
});
