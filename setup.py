from setuptools import setup, find_packages

setup(
    name="BRAT",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "cffi==1.17.1",
        "keyboard==0.13.5",
        "numpy==2.2.6",
        "platformdirs==4.3.8",
        "pycparser==2.22",
        "scipy==1.15.3",
        "sounddevice==0.5.2",
    ],
    entry_points={
        "console_scripts": [
            "BRAT=brat.cli:main",
        ],
    },
    author="bringupyourpost",
    description="BRAT - Bringupyourpost's Recorder Audio Thing",
    long_description=open("README.md").read() if __name__ == "__main__" and open("README.md", "r") else "",
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
)
