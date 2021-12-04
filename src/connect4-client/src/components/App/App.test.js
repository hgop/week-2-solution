import React from "react";
import ReactDOM from 'react-dom';
import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import App from "./App";

it("Should render without crashing", () => {
    const div = document.createElement('div');
    ReactDOM.render(<App />, div);
});

it("Should render texts", () => {
    render(<App />);

    expect(screen.getByText("Connect Four!")).toBeInTheDocument();
    expect(screen.getByText("Join Existing Game")).toBeInTheDocument();
    expect(screen.getByText("Start Local co-op Game")).toBeInTheDocument();
    expect(screen.getByText("Start Multiplayer Game")).toBeInTheDocument();
});

it("Should render input field", () => {
    render(<App />);

    expect(screen.getByText("Connect Four!")).toBeInTheDocument();
    expect(screen.getByText("Join Existing Game")).toBeInTheDocument();
    expect(screen.getByText("Start Local co-op Game")).toBeInTheDocument();
    expect(screen.getByText("Start Multiplayer Game")).toBeInTheDocument();
});
