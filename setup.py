from distutils.core import setup

setup(
    name="aiopyston",
    packages=["pyston"],
    version="1.2.1",
    license="MIT",
    description="An asynchronous API wrapper for the Piston API",
    author="Fang",
    url="https://github.com/ffaanngg/pyston",
    download_url="https://github.com/ffaanngg/pyston/archive/refs/tags/v1.2.1.tar.gz",
    keywords=["Pyston", "Piston API", "API wrapper"],
    package_data={"pyston": ["py.typed"]},
    install_requires=[
        "aiohttp",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
