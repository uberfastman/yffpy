import os
import shutil
import warnings

import setuptools

warnings.warn(
    "yffpy has been DEPRECATED and replaced by yfpy: https://pypi.org/project/yfpy/\nPlease upgrade your project. ",
    DeprecationWarning
)

if os.path.exists("build"):
    print("Removing stale \"build\" directory before packaging...")
    shutil.rmtree("build")

if os.path.exists("dist"):
    print("Removing stale \"dist\" directory before packaging...")
    shutil.rmtree("dist")

if os.path.exists("yffpy.egg-info"):
    print("Removing stale \"yfpy.egg-info\" directory before packaging...")
    shutil.rmtree("yffpy.egg-info")

with open("README.md", "r") as docs:
    long_description = docs.read()

with open("requirements.txt") as reqs:
    required = reqs.read().splitlines()

setuptools.setup(
    name="yffpy",
    version="2.11.0",
    author="Wren J. R.",
    author_email="wrenjr@yahoo.com",
    description="DEPRECATED for https://pypi.org/project/yfpy/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="yahoo fantasy sports api wrapper nfl football nhl hockey mlb baseball nba basketball",
    url="https://github.com/uberfastman/yffpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Console",
        "Intended Audience :: Developers"
    ],
    python_requires=">=3.5",
    install_requires=required
)
