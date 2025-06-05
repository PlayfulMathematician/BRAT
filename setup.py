from setuptools import setup, find_packages

setup(
    name="BRAT",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "sounddevice",
        "numpy",
        "scipy",
        "platformdirs"
    ],
    entry_points={
        "console_scripts": [
            "BRAT=brat.cli:main",  # Uppercase command
        ],
    },
    author="bringupyourpost",
    description="BRAT - Bringupyourpost's Recorder Audio Thing",
    long_description=open("README.md").read() if __name__ == "__main__" and open("README.md", "r") else "",
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
)
