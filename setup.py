import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata_hde", # Replace with your own username
    version="1.0",
    author="Hernan Echeverry",
    author_email="hdmecheverry@gmail.com",
    description="test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hernan_Darius/lambdata_hde",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)