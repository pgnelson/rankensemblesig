from setuptools import setup, find_packages

setup(
    name="rankensemblesig",
    version="0.1.1",
    description="Significance testing for ensembles of rank data",
    author="Paul Nelson",
    author_email="your_email@example.com",
    url="https://github.com/pgnelson/rankensemblesig",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "example-matrix=examples.example_matrix:main",
            "example-list=examples.example_list:main",
        ],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
