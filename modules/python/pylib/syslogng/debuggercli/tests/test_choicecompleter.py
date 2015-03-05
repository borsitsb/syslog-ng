from __future__ import print_function, absolute_import
from .test_completer import TestCompleter
from ..choicecompleter import ChoiceCompleter


class TestChoiceCompleter(TestCompleter):
    def _construct_completer(self, choices=None, prefix=None, suffix=None):
        return ChoiceCompleter(choices or ['foo', 'bar', 'baz'],
                               prefix=prefix,
                               suffix=suffix)

    def test_all_choices_are_offered_for_an_empty_string(self):
        self._completer = self._construct_completer(suffix='')
        self._assert_completions_offered('', ['foo', 'bar', 'baz'])

    def test_only_completions_that_start_with_word_are_listed_as_completions(self):
        for word in ('f', 'b'):
            self._assert_completions_start_with_word(word)

    def test_suffix_is_attached_to_all_potential_matches(self):
        self._completer = self._construct_completer(suffix=' ')
        self._assert_completions_offered('b', ['bar ', 'baz '])
        self._assert_completions_not_offered('b', ['bar', 'baz'])

    def test_prefix_is_attached_to_all_potential_matches(self):
        self._completer = self._construct_completer(prefix='$', suffix='')
        self._assert_completions_offered('$b', ['$bar', '$baz'])
        self._assert_completions_not_offered('$b', ['bar', 'baz'])

    def test_only_prefix_is_offered_if_entire_input_is_shorter(self):
        self._completer = self._construct_completer(prefix='$@', suffix='@')
        self._assert_completion_offered('', '$@')
        self._assert_completion_offered('$', '$@')
        self._assert_completion_not_offered('', '$@bar@')
        self._assert_completion_not_offered('$', '$@bar@')
        self._assert_completions_offered('$@', ['$@foo@', '$@bar@', '$@baz@'])

    def test_not_even_the_prefix_is_offered_if_the_entire_input_diverged_already(self):
        self._completer = self._construct_completer(prefix='$@', suffix='@')
        self._assert_completions_not_offered('q', ['$', '$@', '$@foo@'])
