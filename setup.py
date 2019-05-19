"""Setup script for ``dms_struct``."""


import re
import sys

from setuptools import setup


if not (sys.version_info[0] == 3 and sys.version_info[1] >= 6):
    raise RuntimeError(
                'dms_struct requires Python >=3.6.\n'
                f"You are using {sys.version_info[0]}.{sys.version_info[1]}.")

# get metadata from package `__init__.py` file as here:
# https://packaging.python.org/guides/single-sourcing-package-version/
metadata = {}
init_file = 'dms_struct/__init__.py'
with open(init_file) as f:
    init_text = f.read()
for dataname in ['version', 'author', 'email', 'url']:
    matches = re.findall(
            '__' + dataname + r'__\s+=\s+[\'"]([^\'"]+)[\'"]',
            init_text)
    if len(matches) != 1:
        raise ValueError(f"found {len(matches)} matches for {dataname} "
                         f"in {init_file}")
    else:
        metadata[dataname] = matches[0]

with open('README.rst') as f:
    readme = f.read()

# main setup command
setup(
    name='dms_struct',
    version=metadata['version'],
    author=metadata['author'],
    author_email=metadata['email'],
    url=metadata['url'],
    download_url='https://github.com/jbloomlab/dms_struct/tarball/' +
                 metadata['version'],  # tagged version on GitHub
    description='Visualize deep mutational scanning on protein structure.',
    long_description=readme,
    license='GPLv3',
    install_requires=[
                      'dmslogo>=0.2.3',
                      'matplotlib>=3.0.2',
                      'nglview>=2.0',
                      'numpy>=1.15.4',
                      'pandas>=0.24.2',
                      'pyyaml>=4.2b1',
                      ],
    platforms='Linux and Mac OS X.',
    packages=['dms_struct'],
    package_dir={'dms_struct': 'dms_struct'},
)
