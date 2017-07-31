#!/usr/bin/env python3

from setuptools import setup
import os

__version__ = '0.1.0'

SELF_DIR = os.path.dirname(os.path.abspath(__file__))


def get_full_path(path):
    return os.path.join(SELF_DIR, path)


def read_file(rel_path):
    with open(get_full_path(rel_path)) as reader:
        return reader.read()

required = read_file('requirements.txt').splitlines()

setup(name='Guess-Lyrics-By-Genre',
      version=__version__,
      install_requires=required,
      description="An attempt to guess a song's genre by its lyrics,"
                  "using ML models",
      long_description=read_file('README.md'),
      author='ormatt, Matt Murch',
      author_email='ormatt@outlook.com, mattmurch@gmail.com',
      url='https://github.com/ormatt/Guess-Lyrics-By-Genre',
      download_url='https://api.github.com/repos/ormatt/Guess-Lyrics-By-Genre/tarball/' + __version__,
      scripts=[get_full_path('main.py')],
      license='GPL - 3.0',
      include_package_data=True,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',],
      keywords='lyrics genre guess* ML machine learning model',
      packages=[get_full_path('data_cleaners'),
                get_full_path('feat_exts'),
                get_full_path('transformers'),
                get_full_path('utils'),
                ],
      )
