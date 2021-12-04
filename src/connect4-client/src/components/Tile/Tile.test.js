import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import Tile from './Tile';

it('should render correct number of tiles', () => {
    render(<Tile id={1} tile={1} onClick={(_) => { }} />)

    expect(screen.getAllByLabelText('tile')).toHaveLength(1)
});

it('should render correct className Yellow', () => {
    const { container } = render(<Tile id={1} tile={1} onClick={(_) => { }} />)

    expect(container.firstChild.firstChild).toHaveClass('chip yellow')
});

it('should render correct className Red', () => {
    const { container } = render(<Tile id={2} tile={2} onClick={(_) => { }} />)

    expect(container.firstChild.firstChild).toHaveClass('chip red')
});
