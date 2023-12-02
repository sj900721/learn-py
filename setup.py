from setuptools import setup, find_packages

setup(
    name='greeting_pkg',
    packages=find_packages(),
    version='0.1.0',
    install_requires=[          # 添加了依赖的 package
        'pyjokes'
    ]
)
