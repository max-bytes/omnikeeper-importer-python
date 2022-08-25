from setuptools import setup
setup(
    name='omnikeeper_importer',
    packages=['omnikeeper_importer'],
    version='1.0.0',
    description='Python library containing helper functions for implementing omnikeeper importers',
    author='Maximilian Csuk',
    license='Apache 2.0',
    install_requires=["requests==2.25.1","numpy==1.21.6"]
)