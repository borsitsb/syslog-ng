EXTRA_DIST += \
	modules/python/pylib/debuggercli				\
	modules/python/pylib/debuggercli/commandlinelexer.py		\
	modules/python/pylib/debuggercli/debuglang.py			\
	modules/python/pylib/debuggercli/__init__.py			\
	modules/python/pylib/debuggercli/getoptlexer.py			\
	modules/python/pylib/debuggercli/choicecompleter.py		\
	modules/python/pylib/debuggercli/completer.py			\
	modules/python/pylib/debuggercli/completerlang.py		\
	modules/python/pylib/debuggercli/lexer.py			\
	modules/python/pylib/debuggercli/tests/test_completer.py    \
	modules/python/pylib/debuggercli/tests/test_choicecompleter.py	\
	modules/python/pylib/debuggercli/tests/test_getoptlexer.py	\
	modules/python/pylib/debuggercli/tests/test_completerlang.py	\
	modules/python/pylib/debuggercli/tests/test_lexer.py		\
	modules/python/pylib/debuggercli/tests/test_commandlinelexer.py	\
	modules/python/pylib/setup.py


INSTALL_EXEC_HOOKS += install-pylib

.PHONY: install-pylib
install-pylib:
	(cd $(top_srcdir)/modules/python/pylib && $(PYTHON) setup.py install --prefix $(prefix))
