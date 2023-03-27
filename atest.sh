#!/bin/bash

# 12 Feb 2023 - gswann

# script to assemble atest and convert to mc for 
# loading into z80 computer

joe atest.z80


#cleanup files
rm atest.mc atest.hex atest.lst

grep 'STPR\|CRLF\|XMIT\|PHEX' mm7.lab > atest-mm7.lab

# assemble atest program
z80asm atest.z80 -oatest.hex -latest.lst

# make microcode file
./hexmc atest
