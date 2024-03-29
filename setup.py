from setuptools import setup
import pathlib
from folkol.yg import VERSION

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='folkol.yg',
    version=VERSION,
    description='a unix filter for "greping" in YAML files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/folkol/yg',
    author='folkol',
    author_email='mattias4@kth.se',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Terminals',
        'Topic :: Text Processing :: Filters',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='shell, unix filter',
    packages=["folkol"],
    install_requires=['pyyaml', 'GitPython'],
    python_requires='>=3.6, <4',
    entry_points={
        'console_scripts': [
            'yg=folkol.yg:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/folkol/yg/issues',
        'Source': 'https://github.com/folkol/yg',
    },
)
