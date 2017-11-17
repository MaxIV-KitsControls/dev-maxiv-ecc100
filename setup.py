#!/usr/bin/env python

from setuptools import setup

setup(name = "tangods-ecc100",
      version = "0.1.4",
      description = "Device server for the Attopcube ECC100",
      author = "Mikel Eguiraun",
      author_email = "mikel.eguiraun@maxiv.lu.se",
      license = "GPLv3",
      url = "http://www.maxiv.lu.se",
      packages = ['ecc100'],
      scripts = ['scripts/ECC100']
     )

