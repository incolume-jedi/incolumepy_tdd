"""Test generators."""
import pytest
from incolume.py.tdd.generators import __reference__, generator1

__author__ = "@britodfbr"  # pragma: no cover


def test_path():
    """Test it."""
    assert __reference__ == ''


def test_generator() -> None:
    """Test it."""
    a = generator1([1, 2, 3])
    assert next(a) == 1
