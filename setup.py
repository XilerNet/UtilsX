from distutils.core import setup
from os import path

from utilsx import __version__

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='utilsx',
    packages=['utilsx', 'utilsx.discord', 'utilsx.console'],
    version=__version__,
    license='MIT',
    description='The public Xiler python utility library.',
    project_urls={
        "Documentation": "https://docs.xiler.net/utilsx",
    },
    long_description=long_description,
    author='Xiler Network - Arthurdw',
    author_email='mail.arthurdw@gmail.com',
    url='https://github.com/XilerNet/UtilsX',
    download_url=f'https://github.com/XilerNet/UtilsX/archive/{__version__}.tar.gz',
    keywords=["Xiler", "Utils", "Discord", "Embed", "Formatting", "Console", "Pretty"],
    install_requires=[
        "discord.py"
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        # Development statuses:
        # Development Status :: 1 - Planning
        # Development Status :: 2 - Pre-Alpha
        # Development Status :: 3 - Alpha
        # Development Status :: 4 - Beta
        # Development Status :: 5 - Production/Stable
        # Development Status :: 6 - Mature
        # Development Status :: 7 - Inactive
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
