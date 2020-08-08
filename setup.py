from setuptools import setup
from install import install
setup(
    name='ranger',
    version='0.0.1',
    description='A useful module',
    author='Tom Ben',
    packages=['ranger'],
    install_requires=[
        'pytest',
        'iptcinfo3',
        'mutagen',
        'moviepy',
        'PySide2',
        'tqdm',
        'qdarkstyle'
        ], #external packages as dependencies
    scripts=
    [
    ]
)
install()