# If true, then the svn revision won't be used to calculate the
# revision (set to True for real releases)
import os
RELEASE = False
from tabfix import main

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

# 'setup.py upload' fails on Vista, because .pypirc is searched on 'HOME' path
if not "HOME" in os.environ and  "HOMEPATH" in os.environ:
    os.environ.setdefault("HOME", os.environ.get("HOMEPATH", ""))
    print "Initializing HOME environment variable to '%s'" % os.environ["HOME"]

setup(name="pyftpsync",
      version = main.__version__,
      author = "Martin Wendt",
      author_email = "pyftpsync@wwwendt.de",
      maintainer = "Martin Wendt",
      maintainer_email = "pyftpsync@wwwendt.de",
      url = "http://pyftpsync.googlecode.com/",
      description = "Cleanup whitespace in text files",
      long_description = main.__doc__,

        #Development Status :: 2 - Pre-Alpha
        #Development Status :: 3 - Alpha
        #Development Status :: 4 - Beta
        #Development Status :: 5 - Production/Stable

      classifiers = ["Development Status :: 2 - Pre-Alpha",
                     "Environment :: Console",
                     "Intended Audience :: Information Technology",
                     "Intended Audience :: Developers",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                     "Programming Language :: Python",
                     "Topic :: Software Development :: Libraries :: Python Modules",
                     "Topic :: Utilities",
                     ],
      keywords = "python ftp synchronize tool", 
#      platforms=["Unix", "Windows"],
      license = "The MIT License",
#      install_requires = ["lxml"],
      packages = find_packages(exclude=[]),
      py_modules = ["ez_setup", ],

#      package_data={"": ["*.txt", "*.html", "*.conf"]},
#      include_package_data = True, # TODO: PP
      zip_safe = False,
      extras_require = {},
      test_suite = "tests.test_all.run",
      entry_points = {
          "console_scripts" : ["pyftpsync = tabfix.main:run"],
          },
      )
