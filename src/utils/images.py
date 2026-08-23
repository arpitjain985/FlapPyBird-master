import random
from pathlib import Path
from typing import List, Tuple

import pygame

from .constants import BACKGROUNDS, PIPES, PLAYERS


# Project root:
# FlapPyBird-master/
# ├── assets/
# └── src/
#     └── utils/
#         └── images.py
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SPRITES_DIR = PROJECT_ROOT / "assets" / "sprites"


class Images:
    numbers: List[pygame.Surface]
    game_over: pygame.Surface
    welcome_message: pygame.Surface
    base: pygame.Surface
    background: pygame.Surface
    player: Tuple[pygame.Surface, pygame.Surface, pygame.Surface]
    pipe: Tuple[pygame.Surface, pygame.Surface]

    def __init__(self) -> None:
        # Number sprites: 0.png ... 9.png
        self.numbers = [
            pygame.image.load(
                str(SPRITES_DIR / f"{num}.png")
            ).convert_alpha()
            for num in range(10)
        ]

        # Game over sprite
        self.game_over = pygame.image.load(
            str(SPRITES_DIR / "gameover.png")
        ).convert_alpha()

        # Welcome message sprite
        self.welcome_message = pygame.image.load(
            str(SPRITES_DIR / "message.png")
        ).convert_alpha()

        # Base / ground sprite
        self.base = pygame.image.load(
            str(SPRITES_DIR / "base.png")
        ).convert_alpha()

        # Randomize background, player and pipe
        self.randomize()

    def randomize(self) -> None:
        # Select random background
        rand_bg = random.randint(0, len(BACKGROUNDS) - 1)

        # Select random player
        rand_player = random.randint(0, len(PLAYERS) - 1)

        # Select random pipe
        rand_pipe = random.randint(0, len(PIPES) - 1)

        # Background
        self.background = pygame.image.load(
            str(PROJECT_ROOT / BACKGROUNDS[rand_bg])
        ).convert()

        # Player animation frames
        self.player = (
            pygame.image.load(
                str(PROJECT_ROOT / PLAYERS[rand_player][0])
            ).convert_alpha(),

            pygame.image.load(
                str(PROJECT_ROOT / PLAYERS[rand_player][1])
            ).convert_alpha(),

            pygame.image.load(
                str(PROJECT_ROOT / PLAYERS[rand_player][2])
            ).convert_alpha(),
        )

        # Pipe
        pipe_image = pygame.image.load(
            str(PROJECT_ROOT / PIPES[rand_pipe])
        ).convert_alpha()

        self.pipe = (
            pygame.transform.flip(
                pipe_image,
                False,
                True,
            ),
            pipe_image,
        )
        
