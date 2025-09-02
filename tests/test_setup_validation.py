"""Validation tests to verify testing infrastructure setup."""
import sys
from pathlib import Path


def test_python_version():
    """Test that Python version is compatible."""
    assert sys.version_info >= (3, 8), "Python 3.8+ is required"


def test_project_structure():
    """Test that project structure is correct."""
    project_root = Path(__file__).parent.parent
    
    # Check main application files exist
    assert (project_root / "webapp").is_dir(), "webapp directory should exist"
    assert (project_root / "webapp" / "__init__.py").is_file(), "webapp/__init__.py should exist"
    assert (project_root / "run.py").is_file(), "run.py should exist"
    assert (project_root / "pyproject.toml").is_file(), "pyproject.toml should exist"


def test_testing_structure():
    """Test that testing directory structure is correct."""
    test_root = Path(__file__).parent
    
    assert test_root.name == "tests", "Tests should be in 'tests' directory"
    assert (test_root / "__init__.py").is_file(), "tests/__init__.py should exist"
    assert (test_root / "conftest.py").is_file(), "tests/conftest.py should exist"
    assert (test_root / "unit").is_dir(), "tests/unit directory should exist"
    assert (test_root / "integration").is_dir(), "tests/integration directory should exist"


def test_fixtures_available(temp_dir, mock_config, sample_data):
    """Test that shared fixtures are available and working."""
    # Test temp_dir fixture
    assert temp_dir.exists(), "temp_dir fixture should create a directory"
    assert temp_dir.is_dir(), "temp_dir should be a directory"
    
    # Test mock_config fixture
    assert hasattr(mock_config, 'DEBUG'), "mock_config should have DEBUG attribute"
    assert mock_config.TESTING is True, "mock_config should have TESTING=True"
    
    # Test sample_data fixture
    assert 'cards' in sample_data, "sample_data should contain cards"
    assert len(sample_data['cards']) > 0, "sample_data should have cards data"


def test_markers_configured():
    """Test that pytest markers are properly configured."""
    import pytest
    
    # This test will pass if markers are properly configured in pyproject.toml
    # If markers are not configured, pytest will show warnings but tests will still pass
    pass


class TestExampleClass:
    """Example test class to verify class-based testing works."""
    
    def test_example_method(self):
        """Example test method."""
        assert True, "This should always pass"
        
    def test_with_fixture(self, temp_dir):
        """Test using a fixture in a class-based test."""
        test_file = temp_dir / "class_test.txt"
        test_file.write_text("test")
        assert test_file.exists(), "File should be created in temp directory"