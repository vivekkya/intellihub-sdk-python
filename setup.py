import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="intellihub",
    version="1.4.1",
    author="INTELLIHUB",
    install_requires=[
        "pandas==1.2.3",
        "xlrd==2.0.1",
        "matplotlib==3.3.2",
        "numpy==1.20.2",
        "requests==2.25.1",
        "openpyxl==3.0.7",
        "certifi==2020.12.5",
        "pandas-profiling==2.11.0",
        "seaborn==0.11.1",
        "scikit-learn==0.24.1",
        "autoviz==0.0.81",
        "dtale==1.41.1",
        "umap-learn==0.5.1"
        ],
    author_email="connect@spotflock.com",
    description="Python Client SDK for INTELLIHUB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Spotflock/intellihub-sdk-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
