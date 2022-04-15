from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

pkg_vars = {}
with open('thanosql/version.py') as f:
    exec(f.read(), pkg_vars)

setup(
    name='thanosSQL-magic',
    version=pkg_vars['__version__'],
    description='thanosSQL Ipython Magic',
    long_description=long_description,
    url='http://git.smartmind.team/thanosSQL/thanosweb/thanossql_magic',

    author='Dada Ahn',
    author_email='dada.ahn@smartmind.team',

    license='proprietary',

    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],

    keywords='smartmind thanossql database ipython postgresql',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'ipython',
        'requests',
        'pandas',
    ],

    include_package_data=True,
    zip_safe=False,
)
