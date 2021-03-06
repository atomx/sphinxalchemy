from setuptools import setup
from setuptools import find_packages

version = "0.6.1"

setup(
    name="sphinxalchemy",
    version=version,
    description="SQLAlchemy extension for dealing with SphinxQL",
    long_description=open("README.rst", "r").read(),
    author="Andrey Popp",
    author_email="8mayday@gmail.com",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    zip_safe=False,
    install_requires=[
        "sqlalchemy > 0.9",
    ],
    entry_points="""
    [sqlalchemy.dialects]
    sphinx         = sphinxalchemy.mysqldb:Dialect
    sphinx.cymysql = sphinxalchemy.cymysql:Dialect
    sphinx.mysqldb = sphinxalchemy.mysqldb:Dialect
    sphinx.mysqlconnector = sphinxalchemy.mysqlconnector:Dialect
    """)
