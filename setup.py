import io
import os

import setuptools


setuptools.setup(
    name="kconfiglib",
    # MAJOR.MINOR.PATCH, per http://semver.org
    version="14.1.1a4",
    description="A flexible Python Kconfig implementation",
    # Make sure that README.rst decodes correctly in environments that use
    # the C locale (which implies ASCII), by explicitly giving the encoding.
    long_description=io.open(
        os.path.join(os.path.dirname(__file__), "README.rst"), encoding="utf-8"
    ).read(),
    url="https://github.com/zephyrproject-rtos/Kconfiglib",
    author='Zephyr Project',
    author_email="ci@zephyrproject.org",
    keywords="kconfig, kbuild, menuconfig, configuration-management",
    license="ISC",

    py_modules=(
        "kconfiglib",
        "menuconfig",
        "guiconfig",
        "genconfig",
        "oldconfig",
        "olddefconfig",
        "savedefconfig",
        "defconfig",
        "alldefconfig",
        "allnoconfig",
        "allmodconfig",
        "allyesconfig",
        "listnewconfig",
        "setconfig",
    ),

    entry_points={
        "console_scripts": (
            "menuconfig = menuconfig:_main",
            "guiconfig = guiconfig:_main",
            "genconfig = genconfig:main",
            "oldconfig = oldconfig:_main",
            "olddefconfig = olddefconfig:main",
            "savedefconfig = savedefconfig:main",
            "defconfig = defconfig:main",
            "alldefconfig = alldefconfig:main",
            "allnoconfig = allnoconfig:main",
            "allmodconfig = allmodconfig:main",
            "allyesconfig = allyesconfig:main",
            "listnewconfig = listnewconfig:main",
            "setconfig = setconfig:main",
        )
    },

    # Note: windows-curses is not automatically installed on Windows anymore,
    # because it made Kconfiglib impossible to install on MSYS2 with pip

    python_requires=">=3.9",
    project_urls={
        "GitHub repository": "https://github.com/zephyrproject-rtos/Kconfiglib",
        "Examples": "https://github.com/zephyrproject-rtos/Kconfiglib/tree/master/examples",
    },

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: System :: Operating System Kernels :: Linux",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ]
)
