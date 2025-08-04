# test_middlewarestack.py
"""
Tests for MiddlewareStack module.
"""

import unittest
from middlewarestack import MiddlewareStack

class TestMiddlewareStack(unittest.TestCase):
    """Test cases for MiddlewareStack class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MiddlewareStack()
        self.assertIsInstance(instance, MiddlewareStack)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MiddlewareStack()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
