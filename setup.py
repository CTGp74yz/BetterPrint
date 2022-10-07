from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'A better print function'
LONG_DESCRIPTION = 'Now you can easily print with colors!'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="BetterPrint",
    version=VERSION,
    url='https://github.com/CTGp74yz/BetterPrint',
    author="CTG_Playz",
    author_email="<szimmerman2024@jamesrumsey.net>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],

    keywords=['python', 'print'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education, Programming",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)