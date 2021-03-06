
#
# python setup.py sdist
# python setup.py bdist_dumb
# python setup.py bdist_rpm
#

# follow notes from https://packaging.python.org/distributing/#id69
# and release with `python setup.py sdist upload`

from setuptools import setup, find_packages

setup(
	name = "clc-sdk",
	version = "2.46",
	packages = find_packages("."),

	install_requires = ['prettytable','clint','argparse','requests'],

	entry_points = {
		'console_scripts': [
			'clc  = clc.APIv1.cli:main',
		],
	},


	# metadata for upload to PyPI
	author = "CenturyLink Cloud",
	author_email = "ecosystem@centurylink.com",
	description = "CenturyLink Cloud SDK and CLI",
	keywords = "CenturyLink Cloud SDK CLI",
	url = "https://github.com/CenturyLinkCloud/clc-python-sdk",

	# could also include long_description, download_url, classifiers, etc.
)

