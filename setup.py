from setuptools import setup, find_packages

import incuna_test_utils


setup(
    name='incuna-test-utils'
    packages=find_packages(),
    include_package_data=True,
    version=incuna_test_utils.__version__,
    description='',
    long_description=open('README.rst').read(),
    author=incuna_test_utils.__author__,
    author_email='admin@incuna.com',
    url='https://github.com/incuna/incuna-test-utils/',
    install_requires=[],
    zip_safe=False,
)
