from setuptools import find_packages, setup

setup(
    name="load_sos",
    packages=find_packages(exclude=["load_sos_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
