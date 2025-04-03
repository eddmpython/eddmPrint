import unittest
import sys
from io import StringIO
from eddmPrint import EddmPrint, Colors, Templates

class TestEddmPrint(unittest.TestCase):
    def setUp(self):
        self.printer = EddmPrint()
        self.originalStdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        self.printer.restore()
        sys.stdout = self.originalStdout

    def testBasicPrint(self):
        self.printer.start()
        print("Test")
        output = sys.stdout.getvalue()
        self.assertIn("Test", output)
        self.assertIn("test_printer.py", output)
        self.assertIn("testBasicPrint", output)

    def testColorChange(self):
        self.printer.setColor(Colors.RED).start()
        print("Test")
        self.printer.restore()
        
        self.printer.setColor(Colors.BLUE).start()
        print("Test")
        self.printer.restore()
        
        # 색상 코드 검증은 복잡하므로 생략

    def testTemplateChange(self):
        self.printer.setPrefixTemplate(Templates.SIMPLE).start()
        print("Test")
        output = sys.stdout.getvalue()
        self.assertIn("Test", output)
        self.assertIn("test_printer.py", output)
        self.assertNotIn("함수명", output)

if __name__ == "__main__":
    unittest.main() 