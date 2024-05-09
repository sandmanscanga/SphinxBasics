"""
Module for configuring the Sphinx documentation builder.

Summary:
    This module contains the configuration settings for the Sphinx
    documentation builder. The settings include the project name,
    author, version, and other general settings.

"""

import importlib.util
from datetime import UTC, datetime

project = "Serenity"  # pylint: disable=invalid-name
author = "sandmanscanga"  # pylint: disable=invalid-name

year = datetime.now(UTC).year
if year > 2024:
    # pylint: disable=invalid-name, redefined-builtin
    copyright = f"2024-{year}, {author}"
else:
    copyright = f"2024, {author}"

spec = importlib.util.spec_from_file_location(
    name="serenity", location="../src/serenity/__init__.py"
)

if not spec or not spec.loader:
    raise ImportError("Cannot find serenity module")

mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
release = mod.__version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.imgmath",
    "sphinx.ext.mathjax",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"  # pylint: disable=invalid-name

html_theme = "sphinx_rtd_theme"  # pylint: disable=invalid-name
html_static_path = ["_static"]

todo_include_todos = True  # pylint: disable=invalid-name
