from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='crowemi-py-utils',
    url='https://github.com/crowemi-io/crowemi-py-utils',
    author='Andy Crowe',
    author_email='andy.crowe@crowemi.com',
    packages=['data', 'objects'],
    install_requires=['pymongo', 'models'],
    version='0.1',
    license='MIT',
    description='A collection of utils for interacting with the crowemi-io ecosystem',
    long_description=open('README.md').read(),
)