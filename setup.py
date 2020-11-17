# setuptools setup script.
#
# run as
#   python setup.py sdist --formats=zip
#
from setuptools import setup

setup(
    name = 'pyplotsettings',
    version = '1.0',
    description = 'IEEE friendly pyplot setup',
    url = 'https://jasperdegraaf.nl',
    author = 'Jasper de Graaf',
    author_email = 'j.p.d.graaf@tue.nl',
    license = 'NA',
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Beta',
    ],
    packages = ['pyplotsettings'],
    install_requires = ['matplotlib'],
    python_requires = '>=3',
)