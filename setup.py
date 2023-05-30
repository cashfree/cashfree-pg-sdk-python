from setuptools import setup, find_packages  # noqa: H301

NAME = "cashfree_pg_sdk_python"
VERSION = "2.0.1"
with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()
REQUIRES = ["six >= 1.10", "python-dateutil"]
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

setup(
    name=NAME,
    version=VERSION,
    description="Casfree Payments Payment Gateway Python SDK",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Cashfree Payments",
    author_email="developers@cashfree.com",
    packages=find_packages(),
    url="https://github.com/cashfree/cashfree-pg-sdk-python",
    license="MIT",
    install_requires=REQUIRES,
    keywords=["pg-sdk", "cashfree-pg-sdk", "cashfree", "cashfree-python"],
    include_package_data=True,
)
