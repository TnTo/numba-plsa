import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="numba_plsa",
    version="0.0.1",
    author="Michele Ciruzzi",
    author_email="tnto@hotmail.it",
    description="Numba implementation of PLSA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TnTo/numba-plsa",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    packages=setuptools.find_packages(where=""),
    python_requires=">=3.6",
    install_requires=["numba", "numpy", "scipy"],
)
