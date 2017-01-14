from setuptools import setup

# extract version from __init__.py
with open('localcrawl/__init__.py', 'r') as f:
    version_line = [l for l in f if l.startswith('__version__')][0]
    VERSION = version_line.split('=')[1].strip()[1:-1]


setup(
    name='localcrawl',
    version=VERSION,
    packages=['localcrawl'],
    license='MIT',
    description='Crawl rendered JavaScript templates from a local server.',
    long_description=open('README.rst').read(),
    author='Sven Kreiss',
    author_email='me@svenkreiss.com',
    url='https://github.com/svenkreiss/localcrawl',

    install_requires=[
        'selenium>=2.53.6',
    ],
    extras_require={
        'tests': [
            'hacking>=0.11.0',
            'nose>=1.3.4',
        ]
    },
    entry_points={
        'console_scripts': ['localcrawl=localcrawl.cli:main'],
    },

    tests_require=[
        'nose>=1.3.4',
    ],
    test_suite='nose.collector',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
