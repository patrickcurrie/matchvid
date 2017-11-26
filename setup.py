import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('match-vid/match-vid.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "match-vid",
    packages = ["match-vid"],
    entry_points = {
        "console_scripts": ['match-vid = match-vid.match-vid:main']
        },
    version = version,
    description = "Python command line application for identifying matching keyframes acrosse different videos.",
    long_description = long_descr,
    author = "Patrick Currie",
    author_email = "pcurr303@gmail.com",
    url = "https://github.com/xsec76/match-vid",
)
