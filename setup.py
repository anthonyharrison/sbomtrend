from setuptools import find_packages, setup

# Copyright (C) 2024 Anthony Harrison
# SPDX-License-Identifier: Apache-2.0

from sbomtrend.version import VERSION

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().split("\n")

setup_kwargs = dict(
    name='sbomtrend',
    version=VERSION,
    description='Analyse set of SBOMs to identify changes in components',
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/anthonyharrison/sbomtrend",
    author='Anthony Harrison',
    author_email='anthony.p.harrison@gmail.com',
    maintainer='Anthony Harrison',
    maintainer_email='anthony.p.harrison@gmail.com',
    license='Apache-2.0',
    keywords=["security", "tools", "SBOM", "DevSecOps", "SPDX", "CycloneDX"],
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    python_requires=">=3.8",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sbomtrend = sbomtrend.cli:main",
        ],
    },
)

setup(**setup_kwargs)
