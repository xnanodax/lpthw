try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
#using unittest to test the file instead of nosetests		
	
config = {
	'description': 'ex47 using unittest and using a package',
	'author': 'Cynthia E Ma',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it',
	'author_email': 'missmascience@gmail.com',
	'version': '0.1',
	'install_requires': [''],
	'packages': ['ex47_unittest'], #change
	'scripts': [], #change
	'name': 'ex47_unittest' #change
}
	
setup(**config)
