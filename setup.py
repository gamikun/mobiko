from __future__ import absolute_import
from os.path import join, dirname
from setuptools import setup
import mobiko

basepath = dirname(__file__)
binpath = join(basepath, 'bin')

setup(
  name = 'mobiko',
  packages = ['mobiko'],
  version = mobiko.__version__,
  description = 'Make images for iOS app icon from a big PNG',
  long_description = open(join(basepath, 'README.txt')).read(),
  scripts = [join(binpath, 'mobiko')],
  install_requires=['pillow'],
  author = 'Gamaliel Espinoza M.',
  author_email = 'gamaliel.espinoza@gmail.com',
  url = 'https://github.com/gamikun/mobiko',
  keywords = ['image', 'icons', ''],
  classifiers = [],
)
