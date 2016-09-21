try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
#using nose.tools instead of unittest
	
config = {
	'description': 'ex47 using nosetest and using a package',
	'author': 'Cynthia E Ma',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it',
	'author_email': 'missmascience@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47_nosetests'], #change
	'scripts': [], #change
	'name': 'ex47_nosetests' #change
}
	
setup(**config)
