import React from 'react';
import ReactDOM from 'react-dom';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import LocalCoopGame from './LocalCoopGame';
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
    ReactDOM.render(<LocalCoopGame
        columns={4}
        rows={4}
        client={GameApiClient}
        initialGame={mockGame}
        playerOneId={mockGame.playerOneId}
        playerTwoId={mockGame.playerTwoId}
        handlePlayAgain={(_) => { }}
    />, div);
});

it('should render basic texts', () => {

    render(<LocalCoopGame
        columns={4}
        rows={4}
        client={GameApiClient}
        initialGame={mockGame}
        playerOneId={mockGame.playerOneId}
        playerTwoId={mockGame.playerTwoId}
        handlePlayAgain={(_) => { }}
    />);
    expect(screen.getByText("This is a Local Coop Game")).toBeInTheDocument();
});

it('should render player 1 won text', () => {
    mockGame.winner = 1;

    render(<LocalCoopGame
        columns={4}
        rows={4}
        client={GameApiClient}
        initialGame={mockGame}
        playerOneId={mockGame.playerOneId}
        playerTwoId={mockGame.playerTwoId}
        handlePlayAgain={(_) => { }}
    />);

    expect(screen.getByText("This is a Local Coop Game")).toBeInTheDocument();
    expect(screen.getByText("Player 1!!")).toBeInTheDocument();
    expect(screen.getByText("🐔 🎉 🐔 WINNER WINNER CHICKEN DINNER!!! 🐔 🎉 🎉")).toBeInTheDocument();
});

it('should render player 2 won text', () => {
    mockGame.winner = 2;

    render(<LocalCoopGame
        columns={4}
        rows={4}
        client={GameApiClient}
        initialGame={mockGame}
        playerOneId={mockGame.playerOneId}
        playerTwoId={mockGame.playerTwoId}
        handlePlayAgain={(_) => { }}
    />);

    expect(screen.getByText("This is a Local Coop Game")).toBeInTheDocument();
    expect(screen.getByText("Player 2!!")).toBeInTheDocument();
    expect(screen.getByText("🐔 🎉 🐔 WINNER WINNER CHICKEN DINNER!!! 🐔 🎉 🎉")).toBeInTheDocument();
});

it('should render player 1 turn', () => {
    mockGame.activePlayer = 1;

    render(<LocalCoopGame
        columns={4}
        rows={4}
        client={GameApiClient}
        initialGame={mockGame}
        playerOneId={mockGame.playerOneId}
        playerTwoId={mockGame.playerTwoId}
        handlePlayAgain={(_) => { }}
    />);

    expect(screen.getByText("This is a Local Coop Game")).toBeInTheDocument();
    expect(screen.getByText("It's Player's 1 turn")).toBeInTheDocument();
});

it('should render player 2 turn', () => {
    mockGame.activePlayer = 2;

    render(<LocalCoopGame
        columns={4}
        rows={4}
        client={GameApiClient}
        initialGame={mockGame}
        playerOneId={mockGame.playerOneId}
        playerTwoId={mockGame.playerTwoId}
        handlePlayAgain={(_) => { }}
    />);

    expect(screen.getByText("This is a Local Coop Game")).toBeInTheDocument();
    expect(screen.getByText("It's Player's 2 turn")).toBeInTheDocument();
});

it('should render render play again', () => {
    mockGame.active = false;

    render(<LocalCoopGame
        columns={4}
        rows={4}
        client={GameApiClient}
        initialGame={mockGame}
        playerOneId={mockGame.playerOneId}
        playerTwoId={mockGame.playerTwoId}
        handlePlayAgain={(_) => { }}
    />);

    expect(screen.getByText("Play Again")).toBeInTheDocument();
});
