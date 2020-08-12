#! /bin/bash

echo
read N
echo "ibase=10;obase=2;$N" | bc
