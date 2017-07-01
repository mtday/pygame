
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme_file = f.read()

with open('LICENSE') as f:
    license_file = f.read()

setup(
    name='mygame',
    version='0.0.0',
    description='My Game',
    long_description=readme_file,
    author='Mike Day',
    author_email='mday@eitccorp.com',
    url='https://github.com/mtday/mygame',
    license=license_file,
    install_requires=['pygame'],
    packages=find_packages(exclude=('tests', 'docs'))
)
