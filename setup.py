from setuptools import find_packages, setup

setup(
    name="dagster_titanic",
    packages=find_packages(exclude=["dagster_titanic_tests"]),
    install_requires=[
        "dagster",
        "pandas",
        "pickle",
        "os",
        "numpy",

    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
