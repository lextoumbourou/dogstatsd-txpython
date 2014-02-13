from setuptools import setup, find_packages
import sys


setup(
    name = "dogstatsd-txpython",
    version = "0.3.0",
    author = "Datadog, Inc.",
    author_email = "packages@datadoghq.com",
    description = "Python bindings to Datadog's API and a user-facing command line tool.",
    py_modules=['txstatsd'],
    license = "BSD",
    keywords = "datadog data statsd metrics",
    url = "http://www.datadoghq.com",
)
