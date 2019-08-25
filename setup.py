from setuptools import setup
from setuptools.command.test import test as TestCommand
import codecs
import os
import sys

HERE = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    """Return multiple read calls to different readable objects as a single
    string."""

    return codecs.open(os.path.join(HERE, *parts), 'r', encoding='utf-8').read()


LONG_DESCRIPTION = read('./docs/README.txt')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '--strict',
            '--verbose',
            '--tb=long',
            'tests']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='GS',
    version='0.1.0',
    author='Amey Parundekar',
    author_email='parundekaramey@gmail.com',
    packages=['gs', 'gs.test'],
    license='LICENSE.txt',
    description='Graphics Simulator',
    long_description=LONG_DESCRIPTION,
    tests_require=['pytest', 'pytest-cov', 'pytest-flask==0.14.0'],
    cmdclass={'test': PyTest},
    install_requires=[

    ],
    entry_points={
        'console_scripts': [
            'gsctl = gs.__main__:main'
        ],
    }
)
