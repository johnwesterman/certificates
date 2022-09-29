# Extract certificate bundle into individual certificates with reports

## Simplified step by step for the PCE core install

```
Author: John Westerman
Serial number for this document is Version 1.0 20211102152127;
Version 2021.1
Tuesday November 02, 2021

Things I changed:

#     Updated Wednesday September 28, 2022 22:39
#       1. Accounted for lines too short
#       2. Accounted for lines with spaces
#       3. Don't write lines unless the cert has been found
#       4. Made code/variables easier to read and follow

```

## extract.py

This program will take a standard certificate bundle and break it into it's certificate components and give a breakdown of each certificat issuer and subject.

It will take your PEM formatted file (text) and break it down into individual certificate files (certN.pem). Each file will then have openssl run against it to report it's issuer and subject of the certificates.

The idea is that you can re-create the bundle file any way you may need or learn that the certificate bundle is built properly. Really it's because I'm lazy and don't want to mess with all the commands to validate a certificate to be accurate.
