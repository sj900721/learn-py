from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='greeting_pkg',
    packages=find_packages(),
    version='0.1.0',
    install_requires=[          # 添加了依赖的 package
        'pyjokes'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
