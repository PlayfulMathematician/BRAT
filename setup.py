from setuptools import setup, find_packages

setup(
    name="brat-cli",
    version="0.1.0",
    packages=find_packages(),  # Automatically finds the 'brat' package
    install_requires=[
        "sounddevice",
        "numpy",
        "scipy",
        "platformdirs",  # optional but recommended
    ],
    entry_points={
        "console_scripts": [
            "brat=brat.cli:entry_point",  # Makes `brat` runnable in terminal
        ],
    },
    author="bringupyourpost",
    description="Bringupyourpost's Recorder Audio Thing - CLI for audio recording projects",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
    ],
    include_package_data=True,
)
