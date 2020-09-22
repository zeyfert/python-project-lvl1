"""Brain Even running script."""

from brain_games import engine
from brain_games.games import even


def main():
    """Function to start the Even game"""
    engine.start_game(even)


if __name__ == '__main__':
    main()
