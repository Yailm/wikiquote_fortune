from setuptools import setup, find_packages

setup(
    name="wikiquote_fortune",
    version="0.1",
    packages=find_packages(),
    scripts=['wikiquote_fortune.py'],

    install_requires=['aiohttp', 'lxml'],

    author='Yailm',
    author_email='fiotose@gmail.com',
    url='https://github.com/Yailm/wikiquote_fortune',
    description='Generate fortune cookie from wikiquote',
    license='MIT',

    entry_points={
        "console_scripts": [
            "wikiquote_fortune = wikiquote_fortune:cli"
        ]
    },
    keywords='wikiquote fortune',
)
