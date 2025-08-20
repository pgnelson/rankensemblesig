from setuptools import setup, find_packages

setup(
	name="rankensemblesig",
	version="0.1.0",
	description="Calculates p-values for an ensemble of ranks",
	author="Your Name",
	packages=find_packages(where="src"),
	package_dir={"": "src"},
	install_requires=[
		"pandas",
		"numpy",
		"scipy",
    "math"
	],
	include_package_data=True,
	entry_points={
		"console_scripts": [" = examples.example_load_model:example_load",],
	}
)
