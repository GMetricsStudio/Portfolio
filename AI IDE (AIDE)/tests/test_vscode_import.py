import unittest
import os
from utils.vscode_importer import VSCodeImporter

class TestVSCodeImport(unittest.TestCase):
    def test_importer_init(self):
        importer = VSCodeImporter()
        self.assertTrue(hasattr(importer, 'extensions_path'))
        
    def test_get_extensions_safe(self):
        # Should not crash even if path doesn't exist
        importer = VSCodeImporter()
        # Mock path to something that definitely exists but is empty/not extensions
        importer.extensions_path = os.path.dirname(__file__) 
        exts = importer.get_installed_extensions()
        self.assertIsInstance(exts, list)

if __name__ == '__main__':
    unittest.main()
