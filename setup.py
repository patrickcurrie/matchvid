import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('matchvid/matchvid.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "matchvid",
    packages = ["matchvid"],
    entry_points = {
        "console_scripts": ['matchvid = matchvid.matchvid:main']
        },
    version = version,
    description = "Python command line application for identifying matching keyframes acrosse different videos.",
    long_description = long_descr,
    author = "Patrick Currie",
    author_email = "pcurr303@gmail.com",
    url = "https://github.com/xsec76/matchvid",
)
