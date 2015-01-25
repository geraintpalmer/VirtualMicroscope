from distutils.core import setup

REQUIREMENTS = [
	'Django==1.7.3',
	'Pillow==2.7.0',
	'sphinx_rtd_theme']


setup(
    name='VirtualMicroscope',
    version='0.1dev',
    packages=['virtualmicroscope','nyuvm'],
    license='The MIT License (MIT)',
    install_requires = REQUIREMENTS
    # long_description=open('README.txt').read(),
)