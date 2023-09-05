from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Flask-Caching",
    install_requires=["cachelib == 0.10.2", "Flask < 3"],
)
