from setuptools import find_packages, setup
setup(
    name='omnikeeper_importer',
    packages=find_packages(include=['omnikeeper_importer']),
    version='1.0.0',
    description='Python library containing helper functions for implementing omnikeeper importers',
    author='Maximilian Csuk',
    license='Apache 2.0',
    Install_requires=["requests==2.25.1"]
)