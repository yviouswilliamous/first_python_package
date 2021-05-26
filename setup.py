import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kobefang",
    version="0.0.1",
    author="Yves William OBAME EDOU",
    author_email="yw.obame@gmail.com",
    description="A package with function to speak fang",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yviouswilliamous/first_python_package",
    project_urls={
        "Bug Tracker": "https://github.com/yviouswilliamous/first_python_package/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)