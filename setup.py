from setuptools import setup, find_packages


setup(
    name='incuna-test-utils',
    packages=find_packages(),
    include_package_data=True,
    version='5.1.0',
    description='Custom TestCases and other test helpers for Django apps',
    long_description=open('README.md').read(),
    author='Incuna',
    author_email='admin@incuna.com',
    url='https://github.com/incuna/incuna-test-utils/',
    install_requires=[],
    zip_safe=False,
)
