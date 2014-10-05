from setuptools import setup


setup(

    ### Metadata

    name='Engine',

    version='0.1.0',

    description='Crawl the Web',

    long_description='Crawl the web...',

    url='https://github.com/jakesyl/Engine',

    license='Not Yours',

    author='Jake Sylvestre, Alex Parson ',
    author_email='jakesyl@gmail.com',

    maintainer='Alex Parson, Jake Sylvestre',
    maintainer_email='alexparson1@gmail.com',

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: GIS',
    ],

    ### Dependencies

    install_requires=[
        'utm',
        'SQLAlchemy>=0.6',
        'BrokenPackage>=0.7,<1.0',#change these
    ],

    dependency_links=[
        'git+https://github.com/Turbo87/utm.git@v0.3.1#egg=utm-0.3.1',
    ],

    ### Contents

    packages=find_packages(exclude=['tests*']),

)
