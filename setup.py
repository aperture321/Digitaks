#setup.py
from distutils.core import setup
import py2exe

setup(
      options = {"py2exe": {"bundle_files": 1}},
      console=['Digitaks.py'],
      zipfile = None)