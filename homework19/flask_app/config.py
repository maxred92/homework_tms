import os


class Config:
    PATH = "usr/logs"


class Development(Config):
    DEBUG_MODE = True


class Production(Config):
    DEBUG_MODE = False