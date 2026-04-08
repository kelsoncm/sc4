# -*- coding: utf-8 -*-
from setuptools import setup

# from distutils.core import setup
setup(
    name="sc4net",
    packages=[
        "sc4net",
    ],
    version="0.2.0",
    download_url="https://github.com/kelsoncm/sc4/releases/tag/sc4net-v0.2.0",
    description="Shortcuts for user with Python stdlib HTTP and FTP",
    author="Kelson da Costa Medeiros",
    author_email="kelsoncm@gmail.com",
    url="https://github.com/kelsoncm/sc4",
    keywords=["shortcuts", "http", "ftp", "stdlib"],
    install_requires=["sc4py==0.1.5"],
    classifiers=[],
)
