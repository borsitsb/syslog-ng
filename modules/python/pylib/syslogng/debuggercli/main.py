from __future__ import absolute_import, print_function
from .langcompleter import LangBasedCompleter
from .debuglang import DebugLang
from .templatelang import TemplateLang
from .tflang import TemplateFunctionLang
from .choicecompleter import ChoiceCompleter
from .macrocompleter import MacroCompleter
from .syslognginternals import get_debugger_commands, get_template_functions
import readline
import traceback


class ReadlineCompleteHook(object):
    def __init__(self, completer):
        self._completer = completer
        self._last_contents = (None, None)

    def complete(self, text, state):
        try:
            entire_text = readline.get_line_buffer()[:readline.get_endidx()]
            completions = self._get_completions(entire_text, text)
            return completions[state]
        except Exception as exc:
            traceback.print_exc()

    def _get_completions(self, entire_text, text):
        if (self._last_contents == (entire_text, text)):
            return self._last_completions
        self._last_completions = self._completer.complete(entire_text, text)
        self._last_completions.append(None)
        self._last_contents = (entire_text, text)
        return self._last_completions


template_completers = {}

tflang_completers = {
    'COMMAND': ChoiceCompleter(get_template_functions()),
    'macro': MacroCompleter(),
    'OPT': ChoiceCompleter(('--pair', "--key")),
    'template': LangBasedCompleter(parser=TemplateLang(),
                                   completers=template_completers)
}

template_completers['MACRO'] = MacroCompleter()
template_completers['TEMPLATE_FUNC'] = LangBasedCompleter(
    parser=TemplateFunctionLang(),
    completers=tflang_completers,
    prefix="$(")

debug_completers = {
    'COMMAND': ChoiceCompleter(get_debugger_commands()),
    'template': LangBasedCompleter(parser=TemplateLang(),
                                   completers=template_completers)
}

root_completer = LangBasedCompleter(parser=DebugLang(),
                                    completers=debug_completers)

readline.parse_and_bind("tab: complete")
readline.parse_and_bind(r"\C-o: complete")
readline.set_completer(ReadlineCompleteHook(root_completer).complete)
readline.set_completer_delims(' \t\n\"\'`@><=;|&')

def fetch_command():
    return raw_input("(syslog-ng) ")
