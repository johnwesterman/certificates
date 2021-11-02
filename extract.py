#!/usr/bin/env python3

#
# extract.py - This program will take a standard certificate bundle and break it into
#   it's certificate components and give a breakdown of each certificat issuer and subject.
#
#  Auhor: John Westerman, Tuesday November 02, 2021, Version 1.0 20211102152127
#

import subprocess, sys

if len(sys.argv) < 2:
    print ("I need your certificate chain file as an argument.")
    exit(1)

with open(sys.argv[1], mode="r") as bigfile:

    smallfile_prefix = "cert"
    file_count = 1

    for line in bigfile:
        if line.startswith("-----BEGIN CERTIFICATE-----"):
            smallfile = open(smallfile_prefix + str(file_count), 'w')
            smallfile.write(line)
            file_count += 1
        elif line.startswith("-----END CERTIFICATE-----"):
            smallfile.write(line)
            smallfile.close()
        else:
            smallfile.write(line)

    smallfile.close()

    total_certs = 0
    while total_certs < file_count-1:
        total_certs += 1
        print ("Certificate: %s:" % smallfile_prefix+str(total_certs))
        subprocess.call(["openssl",  "x509", "-noout",  "-subject",  "-issuer", "-in",  smallfile_prefix+str(total_certs)])