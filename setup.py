import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="log3",
    version="0.1.0",
    author="Orlando Diaz",
    author_email="orlandodiaz.dev@gmail.com",
    description="High level logging client builtin support for colored terminal output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/orlandodiaz/log3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ['colorama']

)