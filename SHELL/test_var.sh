#!/bin/bash

NAME="Zara Ali"
echo $NAME
echo $$

a=0
while [ "$a" -lt 50 ]    # this is loop1
do
   b="$a"
   while [ "$b" -ge 0 ]  # this is loop2
   do
      echo -n "$b "
      b=`expr $b - 1`
   done
   echo
   a=`expr $a + 1`
done
