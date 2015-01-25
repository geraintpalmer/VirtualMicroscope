from distutils.core import setup

REQUIREMENTS = [
	'Django==1.7.3',
	'Pillow==2.7.0',
	'sphinx_rtd_theme']


setup(
    name='VirtualMicroscope',
    version='0.1dev',
    packages=['virtualmicroscope','nyuvm'],
    urls = 'https://github.com/evildmp/VirtualMicroscope/tree/hackday',
    license ='The MIT License (MIT)',
    long_description = open('README.txt').read(),
    install_requires = REQUIREMENTS
    # long_description=open('README.txt').read(),
)