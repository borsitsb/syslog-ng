EXTRA_DIST += \
	modules/python/pylib/syslogng/__init__.py				\
	modules/python/pylib/syslogng/debuggercli/__init__.py			\
	modules/python/pylib/setup.py

PYLIB_PATH = modules/python/pylib
PYLIB_BUILDDIR = $(abs_builddir)/$(PYLIB_PATH)
PYLIB_SRCDIR = $(top_srcdir)/modules/python/pylib
SETUPPY_MANIFEST = $(PYLIB_BUILDDIR)/install-manifest.txt
PYTHON_ROOT = $(if $(DESTDIR),$(DESTDIR),/)

INSTALL_EXEC_HOOKS += install-pylib
UNINSTALL_HOOKS += uninstall-pylib
CLEAN_HOOKS += clean-pylib

.PHONY: install-pylib
install-pylib:


	(cd $(PYLIB_SRCDIR) && $(PYTHON) setup.py \
		build --build-base="$(PYLIB_BUILDDIR)/build" \
		install --record=$(SETUPPY_MANIFEST) --root="$(PYTHON_ROOT)" --prefix="$(prefix)")

.PHONY: uninstall-pylib
uninstall-pylib:
	sed -e 's,^,$(PYTHON_ROOT),g' $(SETUPPY_MANIFEST) | tr '\n' '\0' | xargs -0 rm -f


.PHONY: clean-pylib
clean-pylib:
	rm -rf "$(PYLIB_BUILDDIR)/build"
	rm -rf "$(SETUPPY_MANIFEST)"
