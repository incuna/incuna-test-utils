from setuptools import setup, find_packages


setup(
    name='incuna-test-utils',
    packages=find_packages(),
    include_package_data=True,
    version='3.2.0',
    description='icuna-test-utils',
    long_description=open('README.rst').read(),
    author='Incuna',
    author_email='admin@incuna.com',
    url='https://github.com/incuna/incuna-test-utils/',
    install_requires=[],
    zip_safe=False,
)
