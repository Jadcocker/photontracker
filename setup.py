#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Jeremy C. Adcock",
    author_email='jeremy.c.adcock@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="package for simulating interference of quantum photonic pulses in a linear optical circuit, in the time domain",
    entry_points={
        'console_scripts': [
            'photontracker=photontracker.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='photontracker',
    name='photontracker',
    packages=find_packages(include=['photontracker', 'photontracker.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jadcocker/photontracker',
    version='0.0.1',
    zip_safe=False,
)
