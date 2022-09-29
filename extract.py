#!/usr/bin/env python3

#
# extract.py - This program will take a standard certificate bundle and break it into
#   it's certificate components and give a breakdown of each certificat issuer and subject.
#
#  Auhor: John Westerman, Tuesday November 02, 2021
#     Updated Wednesday September 28, 2022 22:39
#       1. Accounted for lines too short
#       2. Accounted for lines with spaces
#       3. Don't write lines unless the cert has been found
#       4. Made code/variables easier to read and follow
#

import subprocess, sys

if len(sys.argv) < 2:
    print ("I need your certificate chain file as an argument.")
    exit(1)

with open(sys.argv[1], mode="r") as certificate_file:

    individual_cert_file_prefix = "cert"
    file_count = 1
    found_beginning = 0

    for line in certificate_file:
        if line.startswith("-----BEGIN CERTIFICATE-----"):
            individual_cert_file = open(individual_cert_file_prefix + str(file_count), 'w')
            individual_cert_file.write(line)
            file_count += 1
            found_beginning = 1
        elif line.startswith("-----END CERTIFICATE-----"):
            individual_cert_file.write(line.strip())
            individual_cert_file.close()
            found_beginning = 0
        elif line.isspace():
            continue
        elif len(line) < 26:
            continue
        else:
            if (found_beginning):
                individual_cert_file.write(line)

    individual_cert_file.close()

    total_certs = 0
    while total_certs < file_count-1:
        total_certs += 1
        print ("Certificate: %s:" % individual_cert_file_prefix+str(total_certs))
        subprocess.call(["openssl",  "x509", "-noout",  "-subject",  "-issuer", "-in",  individual_cert_file_prefix+str(total_certs)])