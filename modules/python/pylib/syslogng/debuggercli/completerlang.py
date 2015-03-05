from __future__ import print_function, absolute_import
import ply.yacc as yacc
import sys
from .tablexer import TabLexer
from abc import abstractmethod, ABCMeta


class CompleterLang(object):
    """Class encapsulating a language (or grammar) used by tab completion

    Derived classes should define their ply.yacc rules in their body, which is
    then translated at instantiation time.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self._parser = yacc.yacc(module=self, write_tables=False)
        self._lexer = TabLexer(self._construct_lexer())

    @abstractmethod
    def _construct_lexer(self):
        raise NotImplementedError

    def get_expected_tokens(self, input, drop_last_token):
        self._lexer.set_drop_last_token(drop_last_token)
        self._parser.parse(input, lexer=self._lexer)
        return self._parser.expected_tokens, self._lexer.get_replaced_token(), self._parser.token_position

    def _collect_expected_productions(self, parser, parser_state, next_state):
        for token, next_next_state in parser.action[next_state].items():
            if next_next_state < 0:
                # production shift, we care about production shifts which would translate the
                # next_state stoken
                production = parser.productions[-next_next_state]
                if production.len and production.name not in parser.expected_tokens:
                    parser.expected_tokens.append(production.name)


    def p_error(self, p):
        parser = self._parser

        if p is None:
            # EOF
            return None
        elif p.type == 'TAB':
            #parser = p.parser

            # This is fragile!
            parser_state = sys._getframe(1).f_locals['state']

            parser.expected_tokens = []
            for token, next_state in parser.action[parser_state].items():
                if token != '$end':
                    parser.expected_tokens.append(token)
                if next_state < 0:
                    production = parser.productions[-next_state]
                    translated_state = parser.statestack[-production.len - 1]
                    try:
                        next_state = parser.action[parser.goto[translated_state][production.name]][token]
                    except KeyError:
                        # this indicates a syntax error, don't add anything
                        continue
                    if next_state < 0:
                        continue
                self._collect_expected_productions(parser, parser_state, next_state)
            parser.token_position = p.lexpos

            parser.errok()
