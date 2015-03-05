import unittest
from ..tflang import TemplateFunctionLang


class TestTFLang(unittest.TestCase):
    def _test_(self):
        self._lang = TemplateFunctionLang()
        tokens = self._lang.get_expected_tokens("format-json ", False)
        self.assertIn("template", tokens)
