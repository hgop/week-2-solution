import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import Board from './Board';

it('should render correct number of columns', () => {
    render(<Board columns={3} rows={4} board={[[], [], []]} onTileClick={(_) => { }} />)

    expect(screen.getAllByLabelText('column')).toHaveLength(3)
});

it('should render correct number of tiles', () => {
    render(<Board columns={2} rows={3} board={[[], []]} onTileClick={(_) => { }} />)

    expect(screen.getAllByLabelText('tile')).toHaveLength(2 * 3)
});
