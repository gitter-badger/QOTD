from setuptools import setup


setup(

    ### Metadata

    name='QOTD',

    version='0.1.0',

    description='Gets a quote, and posts it ',

    long_description='Crawl the web...',

    url='https://github.com/jakesyl/Engine',

    license='Not Yours',

    author='Jake Sylvestre',
    author_email='jakesyl@gmail.com',

    maintainer=' Jake Sylvestre',
    maintainer_email='jakesyl@gmail.com',

    classifiers=[
        'Development Status :: 2 - writing',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: GIS',
    ],

    ### Dependencies

    install_requires=[

    ],

    dependency_links=[
    ],

    ### Contents

    packages=find_packages(exclude=['tests*']),

)
