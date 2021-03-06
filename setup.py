from distutils.core import setup

setup(
  name = 'insteonlocal',
  py_modules = ['insteonlocal'],
  version = '0.21',
  description = 'InsteonLocal allows local (non-cloud) control of the Insteon Hub 2245-222',
  author = 'Michael Long',
  author_email = 'mplong@gmail.com',
  url = 'https://github.com/phareous/insteonlocal',
  download_url = 'https://github.com/phareous/insteonlocal/tarball/0.21',
  keywords = ['insteon'],
  data_files = [('', ['device_models.json', 'device_categories.json'])],
  requires = ['requests', 'time', 'pprint', 'logging', 'logging.handlers', 'sys', 'json', 'collections'],
  provides = ['insteonlocal']
)
