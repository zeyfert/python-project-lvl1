"""Running module for Brain GCD."""

from brain_games import engine
from brain_games.games import gcd


def main():
    """Run GCD game."""
    engine.start_game(gcd)


if __name__ == '__main__':
    main()
