from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    reqs = fh.read().splitlines()

def local_scheme(version):
    return ""

def version_scheme(version):
    return version.tag.base_version

setup(
    name="programmatic_import_demo",
    author="Louis Maddox",
    description=(
        "Reproducible example of a difference in importlib.import_module"
        " and normal relative imports of the format 'from . import foo'"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lmmx/programmatic_import_demo",
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
    ],
    include_package_data=True, # no package data yet but no problem
    use_scm_version={
        "write_to": "version.py",
        "version_scheme": version_scheme,
        "local_scheme": local_scheme,
    },
    setup_requires=["setuptools_scm"],
    python_requires=">=3",
)
