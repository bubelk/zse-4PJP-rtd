# -- Projekt podstawowy -----------------------------------------------------

project = 'Moja Dokumentacja'
author = 'Jakub Prucnal'
release = '1.0'


# -- Konfiguracja Sphinx ----------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = []


# -- Ustawienia HTML --------------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
