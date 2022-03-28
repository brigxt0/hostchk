======
Hostchk
======


.. image:: https://img.shields.io/pypi/v/hostchk.svg
        :target: https://pypi.org/project/hostchk/

.. image:: https://img.shields.io/github/license/brigxt0/webchk.svg
        :target: https://github.com/brigxt0/hostchk/main/LICENSE

hostchk is a command-line tool developed in Python 3 for checking the HTTP
status codes and response headers of URLs. It requires a file of URLs seperated by lines and the name of the file in which to save the output as
arguments. Furthermore, the protocol either https or http can be passed using the -proto option to
process the URLs and check their statuses.


Installation
------------
hostchk is not yet available on PyPI and cant be installed using pip for now



Hostchk does requires 3rd party packages to run. So it can also be
cloned from GitHub and run as::

    $ git clone https://github.com/brigxt0/hostchk.git
    $ cd hostchk
    $ pip3 install requirements.txt
    $ python3 hostchk.py -in <input> -out <output> -proto <protocol>

Usage
-----
::

 hostchk [-h] [-i INPUT] [-o OUTPUT] [-p] [-a] [-l] [-s] [-f] [-v]
              [urls [urls ...]]

 positional arguments:
   urls

 optional arguments:
   -h, --help                   show this help message and exit
   -i INPUT, --input INPUT      Read input from a file
   -o OUTPUT, --output OUTPUT   Save output to a file
   -p, --parse                  Follow links listed in .xml URLs
   -l, --list                   Print URLs without checking them
   -v, --version                Print the version number


Examples
~~~~~~~~
Check a list of URLs from a file (one URL per line)::



Check the status of a sitemap file and all the URLs listed in it::



List the URLs in a file without checking their HTTP status::














