from setuptools import setup, find_packages

setup(
    name="wikiquote_fortune",
    version="0.1",
    packages=find_packages(),
    scripts=['wikiquote_fortune.py'],

    install_requires=['aiohttp', 'lxml'],

    author_email='fiotose@gmail.com',
    description='Generate fortune cookie from wikiquote',
    license='MIT',
    keyword='wikiquote fortune',
)
