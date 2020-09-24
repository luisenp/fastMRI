import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    reqs = []
    for line in f:
        line = line.strip()
        reqs.append(line.split("==")[0])

packages = setuptools.find_packages()
setuptools.setup(
    name="fastmri",
    version="0.1.0",
    author="Facebook AI Research",
    description="fastMRI dataset loaders and baselines.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/facebookresearch/fastMRI/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence :: Medical Imaging",
    ],
    python_requires=">=3.7  ",
    install_requires=reqs,
)
