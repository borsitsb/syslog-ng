from __future__ import absolute_import, print_function
from .. import templatelexer
from .test_lexer import TestLexer


class TestTemplateLexer(TestLexer):

    def _construct_lexer(self):
        return templatelexer.construct_lexer()

    def test_template_literals_are_returned_as_literal_tokens(self):
        self._lexer.input("foobar barfoo")
        token = self._next_token()
        self.assertEquals(token.type, "LITERAL")
        self.assertEquals(token.value, "foobar barfoo")

    def test_template_unbraced_macros_are_returned_as_macros(self):
        self._lexer.input("$MSG")
        token = self._next_token()
        self.assertEquals(token.type, "MACRO")
        self.assertEquals(token.value, "$MSG")

    def test_template_braced_macros_are_returned_as_macros(self):
        self._lexer.input("${MSG}")
        token = self._next_token()
        self.assertEquals(token.type, "MACRO")
        self.assertEquals(token.value, "${MSG}")

    def test_template_simple_template_functions_are_returned_as_template_funcs(self):
        self._lexer.input("$(echo $MSG)")
        token = self._next_token()
        self.assertEquals(token.type, "TEMPLATE_FUNC")
        self.assertEquals(token.value, "$(echo $MSG)")

    def test_template_complex_template_functions_are_returned_as_template_funcs(self):
        self._lexer.input("$(echo $(echo $MSG))")
        token = self._next_token()
        self.assertEquals(token.type, "TEMPLATE_FUNC")
        self.assertEquals(token.value, "$(echo $(echo $MSG))")

    def test_template_even_more_complex_template_functions_are_returned_as_template_funcs(self):
        self._lexer.input("$(grep ('$COUNT' == 5) $MSG)")
        token = self._next_token()
        self.assertEquals(token.type, "TEMPLATE_FUNC")
        self.assertEquals(token.value, "$(grep ('$COUNT' == 5) $MSG)")

    def test_braced_macro_splits_literals_in_half(self):
        self._lexer.input("foobar${MSG}barfoo")
        token = self._next_token()
        self.assertEquals(token.type, "LITERAL")
        self.assertEquals(token.value, "foobar")
        token = self._next_token()
        self.assertEquals(token.type, "MACRO")
        self.assertEquals(token.value, "${MSG}")
        token = self._next_token()
        self.assertEquals(token.type, "LITERAL")
        self.assertEquals(token.value, "barfoo")

    def test_unbraced_macros_split_literals_in_half(self):
        self._lexer.input("foobar $MSG barfoo")
        token = self._next_token()
        self.assertEquals(token.type, "LITERAL")
        self.assertEquals(token.value, "foobar ")
        token = self._next_token()
        self.assertEquals(token.type, "MACRO")
        self.assertEquals(token.value, "$MSG")
        token = self._next_token()
        self.assertEquals(token.type, "LITERAL")
        self.assertEquals(token.value, " barfoo")

    def _test_lexpos(self):
        self.assertTrue(False)

    def test_foo(self):
        self._lexer.input("$(format-json) $")
        token = self._next_token()
        self.assertEquals(token.type, "TEMPLATE_FUNC")
        self.assertEquals(token.value, "$(format-json)")
        self.assertEquals(token.lexpos, 0)
        token = self._next_token()
        self.assertEquals(token.type, "LITERAL")
        self.assertEquals(token.value, " ")
        self.assertEquals(token.lexpos, 14)
        token = self._next_token()
        self.assertEquals(token.type, "LITERAL")
        self.assertEquals(token.value, "$")
        self.assertEquals(token.lexpos, 15)

    def test_foo2(self):
        self._lexer.input("$(format-json)")
        token = self._next_token()
        self.assertEquals(token.type, "TEMPLATE_FUNC")
        self.assertEquals(token.value, "$(format-json)")
        self.assertEquals(token.lexpos, 0)
        token = self._next_token()
        self.assertIsNone(token)
