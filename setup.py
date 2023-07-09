import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="squabbles-client",
    version="0.0.1",
    author="Unkz",
    author_email="",
    description="An API client for squabbles.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/unkz2/squabbles-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
        "pydantic",
        "pydantic-settings",
    ],
    python_requires=">=3.9",
)
