"""
Configuration file for the Sphinx documentation builder.

Summary:
    Configuration file for the Sphinx documentation builder. This
    file contains the project information, the author, the release
    version, and the copyright. It also contains the extensions that
    are used by the documentation builder, the templates path, the
    language, the HTML theme, the static path, and the todo
    extension.

"""

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import importlib.util
import sys
from datetime import UTC, datetime
from importlib.machinery import ModuleSpec

sys.path.insert(0, "../serenity")

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "serenity"  # pylint: disable=invalid-name
author = "sandmanscanga"  # pylint: disable=invalid-name

copyright = (  # pylint: disable=invalid-name, redefined-builtin
    f"{datetime.now(tz=UTC).year}, {author}"
)

spec = importlib.util.spec_from_file_location(
    name="serenity", location="../serenity/__init__.py"
)

if not isinstance(spec, ModuleSpec) or not spec.loader:
    raise ImportError("Could not import serenity")

mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
release = mod.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.imgmath",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"  # pylint: disable=invalid-name

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"  # pylint: disable=invalid-name
html_static_path = ["_static"]

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True  # pylint: disable=invalid-name
