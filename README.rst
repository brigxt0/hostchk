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

hostchk.py [-h] -in INFILE -out OUTPFILE

[-proto PROTOCOL]



options:

  -h, --help       show this help message and exit

  -in INFILE       The input file name

  -out OUTPFILE    The output file name

  -proto PROTOCOL  The protocol to scan with



 
 


Examples
~~~~~~~~























