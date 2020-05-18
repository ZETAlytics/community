import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zetalytics-api",
    version="1.0.1",
    author="Zetalytics",
    author_email="integrations@zetalytics.com",
    description="API wrapper for the Zetalytics Zonecruncher API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZETAlytics/community/tree/master/zetalytics-api/py/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)