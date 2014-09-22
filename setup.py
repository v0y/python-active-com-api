import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
]

setup(
    name='python-active-com-api',
    version='0.0',
    description='Python client for Active.com API ',
    long_description=README,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
    author='Rafał Mirończyk',
    author_email='rafal.mironczyk@lolwtf.pl',
    url='https://github.com/v0y/python-active-com-api',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
