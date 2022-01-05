from distutils.core import setup

setup(
    name='atlassian_marketplace_python_client',
    version='0.2',
    description='The Python Client for the Atlassian Marketplace',
    author='Jean Petry',
    author_email='jpetry@seibert-media.net',
    install_requires=[
        'requests>=2.20.0',
    ],
)
