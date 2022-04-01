=======
Hostchk
=======


.. image:: https://img.shields.io/pypi/v/hostchk.svg
        :target: https://pypi.org/project/hostchk/

.. image:: https://img.shields.io/github/license/brigxt0/webchk.svg
        :target: https://github.com/brigxt0/hostchk/blob/main/LICENSE

hostchk is a python 3 CLI tool for checking the HTTP
status codes and server response headers of URLs.As arguments to the script a file of URLs seperated by lines is required . As well as the name of the file in which to save the output.Note by default the output is saved in the same directory as the input. 
arguments. Furthermore, the protocol either https or http can be passed using the -proto option to
process the URLs and check their statuses.


Installation
------------
hostchk is  available on the python repository, PyPI and can be installed using pip as follows::

 $ pip install hostchk
 

Hostchk requires 3rd party packages to run without which it will not run.It can be cloned from GitHub as::

    $ git clone https://github.com/brigxt0/hostchk.git
    $ cd hostchk
    $ pip3 install -r requirements.txt

Usage
-----
If you installed your hostchk via pip you can run it from any directory as 
::

 hostchk [-h] -in INFILE -out OUTPFILE

 [-proto PROTOCOL]



 options:

   -h, --help       show this help message and exit

   -in INFILE       The input file name

   -out OUTPFILE    The output file name

   -proto PROTOCOL  The protocol to scan with


If you cloned your hostchk directly from Github you can run it as follows::
 $ cd hostchk
 $ python -m  hostchk [-h] -in INFILE -out OUTPFILE
 [-proto PROTOCOL]
 
 

Examples
~~~~~~~~
Run the script installed via pip from a directory containing an arbitrary file of urls named hosts.txt while saving to an output file named status.txt with protocol as https.

::
 $ hostchk -in files -out status
 
Run the script installed via pip from an arbitrary directory which does not contain the input filename named input.txt with protocol set to http.

::
 $ hostchk -in /path/to/input.txt -out /path/to/output. txt -proto http://
 
Run the script cloned from Github as a module inside the hostchk directory for an input.txt in the downloads folder 

::
 $ cd hostchk
 $ python -m hostchk -in ~/storage/downloads/input.txt -out ~/storage/downloads/output.txt

End
---