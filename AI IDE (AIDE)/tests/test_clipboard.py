import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.clipboard_manager import ClipboardManager

class TestClipboardManager(unittest.TestCase):
    def setUp(self):
        self.mock_app = MagicMock()
        self.manager = ClipboardManager(self.mock_app)

    @patch('core.clipboard_manager.HAS_PIL', False)
    @patch('core.clipboard_manager.HAS_WIN32', False)
    def test_get_content_text(self):
        # Mock text clipboard
        self.mock_app.root.clipboard_get.return_value = "Hello World"
        
        content = self.manager.get_content()
        self.assertEqual(content['type'], 'text')
        self.assertEqual(content['data'], "Hello World")
        
    @patch('core.clipboard_manager.HAS_PIL', False)
    @patch('core.clipboard_manager.HAS_WIN32', False)
    def test_get_content_files_from_text(self):
        # Mock file path in clipboard
        # We need a real file path for os.path.exists to work
        real_file = os.path.abspath(__file__)
        self.mock_app.root.clipboard_get.return_value = real_file
        
        content = self.manager.get_content()
        self.assertEqual(content['type'], 'files')
        self.assertEqual(content['data'], [real_file])

    def test_format_for_chat_text(self):
        content = {"type": "text", "data": "Some code"}
        text, display = self.manager.format_for_chat(content)
        self.assertEqual(text, "Some code")
        self.assertIn("Captured text", display)

if __name__ == '__main__':
    unittest.main()
