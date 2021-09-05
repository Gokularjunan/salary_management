from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in salary_management/__init__.py
from salary_management import __version__ as version

setup(
	name="salary_management",
	version=version,
	description="calculates salary",
	author="gokul",
<<<<<<< HEAD
	author_email="gokul2001kit@gmail.com",
=======
	author_email="gokul@gmail.com",
>>>>>>> 04e3750b72244af45d3432551fc768ebdf5a1418
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
