"""
See:
https://github.com/djangothon/django-react-comments
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='django-react-comments',

    version='0.0.2',

    description='Django comment module using in reactJS',
    long_description='Django comment module using in reactJS. Currently only stores to db and uses a dummy user and post.',

    url='https://github.com/djangothon/django-react-comments',

    authors=['Kumar Anirudha', 'Puja Singh'],
    author_email=['anirudhastark@yahoo.com','singhpuja0708@gmail.com'],

    license='MIT',

    classifiers=[
        'Development Status :: 1 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        'License :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='django,comment,module,djangothon,anistark,puja0708,reactJS',

    
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    
    install_requires=[ ],

    
    extras_require={
        
    },

    
    package_data={
        
    },

    
    data_files=[ ],

    
    entry_points={
        
    },
)
