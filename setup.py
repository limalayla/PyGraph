from setuptools import setup
from codecs import open
from os import path

with open('README.md', encoding='utf-8') as f:
	long_desc = f.read()

setup(
	name = 'PyGraph',
	version = '0.5.0',
	description = "Yet another Graph's Theory implementation for Python, this time aimed at readability and ease of use.",
	long_description = long_desc,
	url = "https://github.com/limalayla/PyGraph",
	author = "LimaLayla",
	author_email = "limaantoine@orange.fr",
	license = "MIT",
	keywords = "graph theory implementation lib user-friendly",
	install_requires = ["numpy"],
	packages=["pygraph"],
	
	# From https://pypi.python.org/pypi?%3Aaction=list_classifiers
	classifiers=[
		"Development Status :: 2 - Pre-Alpha",
		"Environment :: Console",
		"Intended Audience :: Education",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Programming Language :: Python :: 3",
		"Topic :: Scientific/Engineering :: Mathematics"
	]
)

