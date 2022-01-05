import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="atlassian_marketplace_python_client",
    version="0.3",
    author="Jean Petry",
    author_email="jpetry@seibert-media.net",
    description="The Python Client for the Atlassian Marketplace",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seibert-media/atlassian_marketplace_python_client",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.0",
    install_requires=[
        "requests>=2.20.0",
    ],
)
