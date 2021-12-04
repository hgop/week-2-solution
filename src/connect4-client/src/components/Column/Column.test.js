import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import Column from './Column';

it('should render correct number of columns', () => {
    render(<Column column={1} rows={4} board={[[], [], []]} onTileClick={(_) => { }} />)

    expect(screen.getAllByLabelText('column')).toHaveLength(1)
});

it('should render correct number of tiles', () => {
    render(<Column column={1} rows={15} board={[[], [], []]} onTileClick={(_) => { }} />)

    expect(screen.getAllByLabelText('tile')).toHaveLength(1 * 15)
});
