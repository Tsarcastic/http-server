"""Setup file for http-server package."""
from setuptools import setup


setup(
    name="http-server",
    description="Python http server for Code Fellows 401",
    author=["Matt Favoino", "Brendan Davis"],
    author_email=["mattfavoino@gmail.com"],
    license="MIT",
    py_modules=["client", "server"],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
    entry_points={
    }
