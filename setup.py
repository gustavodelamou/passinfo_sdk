from setuptools import setup, find_packages

setup(
    name="passinfo_sdk",
    version="1.0.0",
    author="Jean Gustave DELAMOU",
    author_email="jeangustave1996@gmail.com",
    description="A Python SDK for seamless integration with PassInfo API, enabling secure message delivery and contact management",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gustavodelamou/passinfo_sdk",
    packages=find_packages(exclude=["tests*", "examples*"]),
    install_requires=[
        "requests>=2.25.1",
        "urllib3>=2.0.0",
        "cryptography>=3.4.7",
        "certifi>=2021.5.30",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security",
    ],
    project_urls={
        "Bug Reports": "https://github.com/gustavodelamou/passinfo_sdk/issues",
        "Documentation": "https://github.com/gustavodelamou/passinfo_sdk/wiki",
        "Source Code": "https://github.com/gustavodelamou/passinfo_sdk",
    },
    keywords="api, sdk, messaging, security, passinfo, sms",
    package_data={
        "passinfo_sdk": ["py.typed", "*.pyi", "**/*.pyi"],
    },
    zip_safe=False,
    include_package_data=True,
)