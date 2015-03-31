#!/bin/sh
# flashes an elf, either via a running openocd, or by firing up a new one.
# Originally sourced from a makefile snippet from:
# https://gist.github.com/projectgus/8dab3f891c9bd694fc5f

ELF=$1
( echo "halt; program ${ELF}; reset" | nc localhost 4444 ) || \
    openocd --command "program ${ELF} verify reset exit"
