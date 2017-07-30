#!/usr/bin/env python3

from setuptools import setup
import os

__version__ = '0.1.0'

SELF_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(SELF_DIR, 'requirements.txt')) as reader:
    required = reader.read().splitlines()

setup(name='Guess-Lyrics-By-Genre',
      version=__version__,
      install_requires=required,
      description="An attempt to guess a song's genre by its lyrics,"
                  "using ML models",
      long_description=open(os.path.join(SELF_DIR, 'README.md')).read(),
      author='ormatt, Matt Murch',
      author_email='ormatt@outlook.com, mattmurch@gmail.com',
      url='https://github.com/ormatt/Guess-Lyrics-By-Genre',
      download_url='https://api.github.com/repos/ormatt/Guess-Lyrics-By-Genre/tarball/' + __version__,
      scripts=['main.py'],
      license='GPL - 3.0',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',],
      keywords='lyrics genre guess* ML machine learning model',
      packages=['data',
                'data_cleaners',
                'feat_exts',
                'resources',
                'transformers',
                'utils',
                ],
      )
