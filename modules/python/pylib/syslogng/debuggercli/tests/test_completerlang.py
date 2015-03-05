from __future__ import absolute_import, print_function
import unittest
from ..debuglang import DebugLang
from syslogng.debuggercli.commandlinelexer import CommandLineLexer


class _TestCompleterLang(unittest.TestCase):
    def setUp(self):
        self._parser = DebugLang()

    def test_parser_command_is_expected_as_first_token(self):
        expected_tokens = self._parser.get_expected_tokens("", drop_last_token=False)
        self.assertIn('COMMAND', expected_tokens)

    def test_parser_arg_or_template_is_expected_as_first_argument_to_print(self):
        expected_tokens = self._parser.get_expected_tokens("print", drop_last_token=False)
        self.assertIn('ARG', expected_tokens)
        self.assertIn('template', expected_tokens)

    def _test_parser_nothing_is_expected_as_first_argument_to_print(self):
        expected_tokens = self._parser.get_expected_tokens("print $MSG", drop_last_token=False)
        self.assertEquals([], expected_tokens)
