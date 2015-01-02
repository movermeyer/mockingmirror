from setuptools import setup
from codecs import open
import os

here = os.path.abspath(os.path.dirname(__file__))

def read_file(*names):
    file_path = os.path.join(here, *names)
    with open(file_path, encoding="utf-8") as f:
        return f.read()

def exec_file(*names):
    code = read_file(*names)
    result = {}
    exec(code, result)
    return result

setup(
    name="mockingmirror",
    version=exec_file("mockingmirror.py")["__version__"],
    description="Make strict mocks using a mirror",
    long_description=read_file("README.rst"),
    url="https://github.com/NegativeMjark/mockingmirror",
    author="Mark Haines",
    author_email="mjark@negativecurvature.net",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
    ],
    keywords="mock",
    install_requires=["mock"],
)
