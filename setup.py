from setuptools import setup, find_packages

setup(
    name="thumbor_request_modifier",
    version="2.0.4",
    author="DFFRNT Lab",
    description=("Thumbor HTTP loader which allows modifying the client request based on certain conditions."),
    license="GPLv3",
    keywords=['thumbor', 'request modifier'],
    url="https://github.com/dffrntmedia/thumbor-request-modifier",
    packages = ['thumbor_request_modifier'],
    install_requires=[
        "thumbor==7.*,>=7.0.6",
        "tornado==6.*,>=6.0.3"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
    ],
)
