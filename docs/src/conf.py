"""Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""  # noqa: INP001

import datetime
import importlib.metadata
import pathlib
import tomllib

PROJECT_ROOT_DIR = pathlib.Path(__file__).parent.parent.parent

with (PROJECT_ROOT_DIR / "pyproject.toml").open("rb") as f:
    data = tomllib.load(f)
    project_name = data["project"]["name"]
    project_author = data["project"]["authors"][0]["name"]
    project_version = importlib.metadata.version(project_name)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = project_name
author = project_author
copyright = f"{datetime.datetime.now(tz=datetime.UTC).year}, {author}"  # noqa: A001
release = project_version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
]
templates_path = ["_templates"]

napoleon_google_docstring = False
napoleon_include_private_with_doc = True
napoleon_use_admonition_for_notes = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "furo"
# html_logo = ...  # noqa: ERA001
html_theme_options = {
    "sidebar_hide_name": True,
}
