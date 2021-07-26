import os

class Config(object):
    """Base configuration"""
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@172.18.0.3:5432/operations"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Production configuration"""


class DevelopmentConfig(Config):
    """Development configuration"""


class TestingConfig(Config):
    """Testing configuration"""

    TESTING = True
    