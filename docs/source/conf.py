"""
Module to configure the Sphinx documentation builder.

Summary:
    This module is used to configure the Sphinx documentation
    builder. It is used to set the project name, author, version,
    and other settings. It also sets the path to the project source
    code so that the documentation can be built.

"""

import importlib.util
import os
import sys
from datetime import UTC, datetime

sys.path.insert(0, os.path.abspath("../../"))

project = "serenity"  # pylint: disable=invalid-name
author = "sandmanscanga"  # pylint: disable=invalid-name

year = datetime.now(UTC).year
copyright = (  # pylint: disable=invalid-name, redefined-builtin
    f"{year}, {author}"
)

spec = importlib.util.spec_from_file_location(
    name="serenity", location="../../serenity/src/serenity/__init__.py"
)
if not spec or not spec.loader:
    raise ImportError("Cannot find the serenity package")

mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

release = mod.__version__  # pylint: disable=invalid-name

extensions = [
    "sphinx.ext.autodoc",  # Includes documentation from docstrings
    "sphinx.ext.coverage",  # Checks documentation coverage
    "sphinx.ext.napoleon",  # Parses Google style docstrings
    "sphinx.ext.viewcode",  # Includes links to source code
]

templates_path = ["_templates"]

html_theme = "sphinx_rtd_theme"  # pylint: disable=invalid-name
html_static_path = ["_static"]

# Napoleon settings
napoleon_google_docstring = True  # pylint: disable=invalid-name
