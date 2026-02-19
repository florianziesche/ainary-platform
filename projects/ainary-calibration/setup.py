"""
Setup file for Ainary Calibration Library
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="ainary-calibration",
    version="0.1.0",
    description="Trust Calibration Methods for LLM Agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ainary Research",
    author_email="research@ainary.com",
    url="https://github.com/ainary/calibration",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.0",
    ],
    extras_require={
        "viz": ["matplotlib>=3.7.0"],
        "ml": ["scikit-learn>=1.3.0"],
        "llm": ["openai>=1.0.0", "anthropic>=0.18.0"],
    },
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="calibration, confidence, llm, agents, uncertainty, trust",
    project_urls={
        "Bug Reports": "https://github.com/ainary/calibration/issues",
        "Source": "https://github.com/ainary/calibration",
        "Documentation": "https://github.com/ainary/calibration#readme",
    },
)
