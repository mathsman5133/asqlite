from setuptools import setup, Command
import os

readme = ""
with open("README.rst") as f:
    readme = f.read()

setup(
    name="asqlite",
    author="Rapptz",
    url="https://github.com/Rapptz/asqlite",
    packages=["aslite"],
    license="MIT",
    description="A simple async wrapper for sqlite3",
    long_description=readme,
    python_requires=">=3.5.3",
    classifiers={
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    },
)