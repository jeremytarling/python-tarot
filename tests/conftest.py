"""Shared pytest fixtures for the test suite."""
import os
import tempfile
from pathlib import Path
from unittest.mock import MagicMock

import pytest


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def temp_file(temp_dir):
    """Create a temporary file for testing."""
    temp_file = temp_dir / "test_file.txt"
    temp_file.write_text("test content")
    yield temp_file


@pytest.fixture
def mock_config():
    """Mock configuration object for testing."""
    config = MagicMock()
    config.DEBUG = False
    config.TESTING = True
    config.SECRET_KEY = "test-secret-key"
    return config


@pytest.fixture
def mock_flask_app():
    """Mock Flask app instance for testing."""
    app = MagicMock()
    app.config = {
        'TESTING': True,
        'DEBUG': False,
        'SECRET_KEY': 'test-secret-key'
    }
    return app


@pytest.fixture(autouse=True)
def clean_environment():
    """Clean up environment variables before and after each test."""
    original_env = dict(os.environ)
    yield
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def sample_data():
    """Provide sample data for testing."""
    return {
        "cards": [
            {"name": "The Fool", "number": 0},
            {"name": "The Magician", "number": 1},
            {"name": "The High Priestess", "number": 2}
        ]
    }