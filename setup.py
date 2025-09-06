# setup.py

from setuptools import setup, find_packages

setup(
    name="heartcli",
    version="0.1",
    packages=find_packages(),  # automatically find packages in your project
    install_requires=[
        "rich",
        "prompt_toolkit",
        "requests",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "heartcli = cli.main:main"
        ]
    },
    author="Your Name",
    description="Heart Disease Detection CLI Tool Demo",
    python_requires=">=3.8",
)
