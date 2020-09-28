from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="products",
    version="0.1.0",
    packages=["products",],
    install_requires=["parts",],
    license="MIT",
    url="https://github.com/lapets/products",
    author="Andrei Lapets",
    author_email="a@lapets.io",
    description="Simple function for building ensembles of iterables "+\
                "that are disjoint partitions of an overall Cartesian "+\
                "product.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    test_suite="nose.collector",
    tests_require=["nose"],
)
