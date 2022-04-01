from setuptools import setup
import versioneer
import pathlib


here = pathlib.Path(__file__).parent.resolve()
big_desc = (here / "README.rst").read_text(encoding="utf-8")


#with open('README.rst') as readme_file:
    #readme = readme_file.read()

#with open('HISTORY.rst') as history_file:
    #history = history_file.read()

setup(
    name='hostchk',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=['hostchk'],
    test_suite='test',
    url='https://github.com/brigxt0/hostchk/',
    license="MIT license",
    author='brigxt0 (◣_◢)ⱤEViⱠ(◣_◢)',
    description='A command-line tool for checking HTTP status codes and ' +
                ' server response headers of URLs',
    long_description_content_type="text/x-rst" ,
    long_description=big_desc , 
    keywords='hostchk site management www http link check',
    zip_safe=False,
    include_package_data=False,
    python_requires=">=3.7, <4",
    install_requires=["requests==2.26.0",                              "rich==12.0.1",                                  "tqdm==44.62", 
                      "urllib3==1.26.7"
                      ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
    ],

    entry_points={
        'console_scripts': [
            'hostchk = hostchk.__main__:main',
        ]
    },
)