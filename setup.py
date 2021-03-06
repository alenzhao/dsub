"""setuptools-based installation script.

File is based on this template: https://github.com/pypa/sampleproject
"""

import unittest
# Always prefer setuptools over distutils
from setuptools import find_packages
from setuptools import setup


def unittest_suite():
  """Get test suite (Python unit tests only)."""
  test_loader = unittest.TestLoader()
  test_suite = test_loader.discover('test/unit', pattern='test_*.py')
  return test_suite


setup(
    name='dsub',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.0',
    description=('A command-line tool that makes it easy to submit and run'
                 ' batch scripts in the cloud'),

    # The project's main homepage.
    url='https://github.com/googlegenomics/dsub',

    # Author details
    author='Google',
    # author_email='pypa-dev@googlegroups.com',  ??

    # Choose your license
    license='Apache',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: ',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: System :: Distributed Computing',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='cloud bioinformatics',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        # dependencies for dsub, ddel, dstat
        'google-api-python-client',
        'oauth2client',
        'python-dateutil',
        'pytz',
        'pyyaml',
        'tabulate',

        # dependencies for test code
        'parameterized',
    ],

    # Define a test suite for Python unittests only.
    test_suite='setup.unittest_suite',

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #     'sample': ['package_data.dat'],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa  # pylint: disable=line-too-long
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # 'scripts' keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'dsub=dsub.commands.dsub:main',
            'dstat=dsub.commands.dstat:main',
            'ddel=dsub.commands.ddel:main',
        ],
    },)
