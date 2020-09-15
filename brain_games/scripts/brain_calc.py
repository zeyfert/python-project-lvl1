"""Running script for Brain Calc."""

from brain_games import engine
from brain_games.games import calc


def main():
    """Method to run Calc game."""
    engine.start_game(calc)


if __name__ == '__main__':
    main()
