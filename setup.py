import re
import ast
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('spidertreepy/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='SpiderTreePy',
    version=version,
    url='',
    license='MIT',
    author='Vadim Gorbachev',
    author_email='bmsdave@gmail.com',
    description='',
    long_description=__doc__,
    packages=['spidertreepy'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        "beautifulsoup4 = 4.6.0",
        "numpy = 1.12.1",
        "pandas = 0.20.1",
        'tensorflow>=1.15.2'
        "selenium = 3.4.2",
        "pdfminer.six = 20170419"
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points='''
        [console_scripts]
    '''
)
