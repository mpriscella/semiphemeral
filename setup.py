import setuptools
import semiphemeral

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="semiphemeral",
    version=semiphemeral.version,
    author="Micah Lee",
    author_email="micah@micahflee.com",
    long_description=long_description,
    description="Automatically delete your old tweets, except for the ones you want to keep",
    long_description_content_type="text/markdown",
    license="GPLv3+",
    url="https://github.com/micahflee/semiphemeral",
    packages=['semiphemeral'],
    classifiers=(
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ),
    entry_points={
        'console_scripts': [
            'semiphemeral = semiphemeral:main',
        ],
    },
    install_requires=[
        'click',
        'colorama',
        'python-twitter',
        'flask',
        'sqlalchemy'
    ]
)
