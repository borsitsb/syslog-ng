from     __future__ import print_function, absolute_import
from .completerlang import CompleterLang
from .commandlinelexer import CommandLineLexer
from .getoptlexer import GetoptLexer


class TemplateFunctionLang(CompleterLang):
    tokens = [
        "COMMAND", "ARG", "COMMAND_FORMAT_JSON", "COMMAND_ECHO", "COMMAND_GEOIP", "OPT_KEY", "OPT_PAIR", "OPT"
    ]

    def p_template_func(self, p):
        '''template_func : tf_format_json
                         | tf_echo
                         | tf_geoip
                         | tf_generic'''
        pass

    def p_tf_format_json(self, p):
        '''tf_format_json : COMMAND_FORMAT_JSON tf_format_json_args'''
        pass

    def p_tf_format_json_args(self, p):
        '''tf_format_json_args : OPT_PAIR ARG
                               | OPT_KEY macro
                               | OPT
                               | args'''
        pass

    def p_macro(self, p):
        '''macro : ARG'''
        pass

    def p_tf_echo(self, p):
        '''tf_echo : COMMAND_ECHO template'''
        pass

    def p_tf_geoip(self, p):
        '''tf_geoip : COMMAND_GEOIP ipaddress'''
        pass

    def p_tf_generic(self, p):
        '''tf_generic : COMMAND args'''
        pass

    def p_args(self, p):
        '''args : ARG args
                |
        '''
        pass

    def p_template(self, p):
        '''template : ARG'''
        pass

    def p_ipaddress(self, p):
        '''ipaddress : ARG'''
        pass

    def _construct_lexer(self):
        return GetoptLexer(CommandLineLexer(), known_commands=("format-json", "echo", "geoip"))