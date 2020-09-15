#!/usr/bin/env python3

from brain_games import engine
from brain_games.games import prime

"""Running module for Brain Prime."""


def main():
    """Run Prime game"""
    engine.start_game(prime)


if __name__ == '__main__':
    main()
