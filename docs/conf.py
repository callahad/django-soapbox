import os

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'django-soapbox'
copyright = u'2011-2017, James Bennett'
version = '1.5'
release = '1.5'
exclude_trees = ['_build']
pygments_style = 'sphinx'
html_static_path = ['_static']
htmlhelp_basename = 'django-soapboxdoc'
latex_documents = [
  ('index', 'django-soapbox.tex', u'django-soapbox Documentation',
   u'James Bennett', 'manual'),
]
if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

