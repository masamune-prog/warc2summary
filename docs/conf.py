"""Sphinx configuration."""
project = "warc2summary"
author = "masamune-prog"
copyright = "2024, masamune-prog"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
