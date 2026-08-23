import sys
from pathlib import Path

import pygame


# Project root:
# FlapPyBird-master/
# ├── assets/
# ├── src/
# └── main.py
PROJECT_ROOT = Path(__file__).resolve().parents[2]
AUDIO_DIR = PROJECT_ROOT / "assets" / "audio"


class Sounds:
    die: pygame.mixer.Sound
    hit: pygame.mixer.Sound
    point: pygame.mixer.Sound
    swoosh: pygame.mixer.Sound
    wing: pygame.mixer.Sound

    def __init__(self) -> None:
        # Windows uses WAV files in this project.
        # Linux/macOS uses OGG files.
        if sys.platform.startswith("win"):
            ext = "wav"
        else:
            ext = "ogg"

        self.die = pygame.mixer.Sound(
            str(AUDIO_DIR / f"die.{ext}")
        )

        self.hit = pygame.mixer.Sound(
            str(AUDIO_DIR / f"hit.{ext}")
        )

        self.point = pygame.mixer.Sound(
            str(AUDIO_DIR / f"point.{ext}")
        )

        self.swoosh = pygame.mixer.Sound(
            str(AUDIO_DIR / f"swoosh.{ext}")
        )

        self.wing = pygame.mixer.Sound(
            str(AUDIO_DIR / f"wing.{ext}")
        )









# import sys

# import pygame


# class Sounds:
#     die: pygame.mixer.Sound
#     hit: pygame.mixer.Sound
#     point: pygame.mixer.Sound
#     swoosh: pygame.mixer.Sound
#     wing: pygame.mixer.Sound

#     def __init__(self) -> None:
#         if "win" in sys.platform:
#             ext = "wav"
#         else:
#             ext = "ogg"

#         self.die = pygame.mixer.Sound(f"assets/audio/die.{ext}")
#         self.hit = pygame.mixer.Sound(f"assets/audio/hit.{ext}")
#         self.point = pygame.mixer.Sound(f"assets/audio/point.{ext}")
#         self.swoosh = pygame.mixer.Sound(f"assets/audio/swoosh.{ext}")
#         self.wing = pygame.mixer.Sound(f"assets/audio/wing.{ext}")
