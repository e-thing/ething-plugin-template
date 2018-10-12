
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import os
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open
import json

here = os.path.abspath(os.path.dirname(__file__))

NAME = 'ething_plugin_template'

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the version number from the plugin.json file
with open(os.path.join(here, 'plugin.json'), encoding='utf-8') as f:
    try:
        metadata = json.load(f)
    except:
        metadata = {
            'version': '0.0.1'
        }


setup(
    name='ething-plugin-template',

    version=metadata.get('version'),

    description='ething plugin template',

    long_description=long_description,

    long_description_content_type='text/markdown',

    keywords='ething plugin template',
    
    package_dir={NAME: ''},

    packages=[NAME],
    
    include_package_data=True,

    install_requires=[]
)
