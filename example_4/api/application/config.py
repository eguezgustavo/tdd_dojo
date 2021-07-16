import os

class Config(object):
    """Base configuration"""
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/operations"

class ProductionConfig(Config):
    """Production configuration"""


class DevelopmentConfig(Config):
    """Development configuration"""


class TestingConfig(Config):
    """Testing configuration"""

    TESTING = True
    