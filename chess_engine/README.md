# Module Structure

<!--toc:start-->
- [Module Structure](#module-structure)
  - [core/](#core)
  - [board/](#board)
  - [move_generation/](#movegeneration)
  - [utils/](#utils)
  - [Example](#example)
<!--toc:end-->

### core/

The core module contains fundamental components used throughout the engine.

- `interfaces/`: Abstract base classes for defining the interfaces for major components.
  - `board_interface.py`: Defines the `IBoardState` interface for board representation.
  - `move_generator_interface.py`: Defines the `IMoveGenerator` interface for move generation.

- `models/`: Data classes representing core chess concepts.
  - `piece.py`: Represents a chess piece.
  - `square.py`: Represents a square on the chess board.
  - `move.py`: Represents a chess move.

- `enums.py`: Enumerations for piece types, colours and other constants.

### board/

This module handles the representation of the chess board.

- `board_state.py`: Implements the `BoardState` class, which represents the current state of the chess board

### move_generation/

This module is responsible for generating legal moves.

- `move_generator.py`: Implements the `MoveGenerator` class, which generates legal moves for a given board state.
- `move_validators/`: Contains validators for generating moves for specific piece types.
        - `base_validator.py`: Defines the `BaseValidator` abstract base class.
        - `pawn_validator.py`: Implements move generation for pawns.

### utils/

Utility functions and classes used across the engine.

- `logger.py`: Provides logging functionality for the engine.

## Example

```python
from chess_engine.board.board_state import BoardState
from chess_engine.core.move_generation.move_generator import MoveGenerator
from chess_engine.core.models.square import Square
from chess_engine.core.enums import Colour, PieceType

# Create a new board
board = BoardState()

# Set up the initial positions of all pieces
board.set_initial_position()

# Create a move generator
move_generator = MoveGenerator()

# Generate legal moves for the current position
legal_moves = move_generator.generate_legal_moves(board)

# Print the number of legal moves
print(f"Number of legal moves: {len(legal_moves)}")
```
