import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

install_requires = []

tests_require = [
    'nose2==0.5'
]

setup(
    name='python-active-com-api',
    version='0.1.1',
    description='Python client for Active.com API ',
    long_description=open(os.path.join(here, 'README.md')).read(),
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
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='nose2.collector.collector',
)
