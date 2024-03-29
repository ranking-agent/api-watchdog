from setuptools import setup, find_packages


def readme():
    """Get readme text."""
    with open("README.md") as f:
        return f.read()


def version():
    """Get version number."""
    with open("VERSION") as f:
        return f.read()


setup(
    name="api_watchdog",
    version=version(),
    packages=find_packages(),
    license="MIT",
    author="CoVar",
    description="API watchdog",
    long_description=readme(),
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": [
        'api-watchdog = api_watchdog.cli:cli'
    ]}
)
