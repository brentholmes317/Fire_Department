try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description' : 'A program to determine the best spot for a fire department.',
  'author' : 'Brent Holmes',
  'url' : 'n/a',
  'download_url' : 'n/a',
  'author_email' : 'brentholmes@ku.edu',
  'version' : '0.1',
  'install_requires' : ['nose'],
  'packages' : ['fire_department', 'fire_department_list', 'fire_department_file']
  'scripts' : [],
  'name' : 'fire_department'
}

setup(**config)
