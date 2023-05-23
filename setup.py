import os
from setuptools import find_packages, setup


def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path), encoding="utf-8") as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


# Package meta-data.
NAME = "cloudmonitor"
DESCRIPTION = "A Web-GUI Monitor for Academic Linux Servers"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = get_version("cloudmonitor/__init__.py")


# BEFORE importing setuptools, remove MANIFEST. Otherwise it may not be
# properly updated when the contents of directories change (true for distutils,
# not sure about setuptools).
if os.path.exists("MANIFEST"):
    os.remove("MANIFEST")

# What packages are required for this module to be executed?
# `estimator` may depend on other packages. In order to reduce dependencies, it is not written here.
REQUIRED = [
    "flask>=2.0.0",
    "paramiko>=3.0.0",
    "pyyaml>=6.0",
    "gevent>=22.10.2",
]

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "PACKAGE.md"), encoding="utf-8") as f:
    long_description = f.read()


if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION,
        license="MIT Licence",
        url="https://github.com/WNJXYK/cloudmonitor",
        packages=find_packages(),
        include_package_data=True,
        author="Zhi Zhou",
        author_email="wnjxyk@gmail.com",
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type="text/markdown",
        python_requires=REQUIRES_PYTHON,
        install_requires=REQUIRED,
        classifiers=[
            "Intended Audience :: Science/Research",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Topic :: Software Development",
            "Topic :: Scientific/Engineering",
            "Operating System :: POSIX :: Linux",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: MacOS",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        entry_points={
            'console_scripts': [
                'cloudmonitor  = cloudmonitor:main',
                'cloud-monitor = cloudmonitor:main',
            ]
        }
    )
