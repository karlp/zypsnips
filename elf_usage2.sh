#!/bin/sh
# Karl Palsson 2022
[ -f $1 ] || {
	printf "Needs an elf to work on!"
	return 1
}
RAM=${2:-2}
FLASH=${3:-0}
NM=${NM:-arm-none-eabi-nm}
${NM} -S $1 | sed -e "s/^${FLASH}[0-9a-f]\{7\}/flash\t&/" | sed -e "s/^${RAM}[0-9a-f]\{7\}/ram\t&/" | sort -k1,1 -k3,3
