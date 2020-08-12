from setuptools import setup
import os

readme = ""
with open("README.md") as f:
    readme = f.read()

setup(
    name="asqlite",
    author="Rapptz",
    url="https://github.com/Rapptz/asqlite",
    packages=["asqlite.py"],
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
