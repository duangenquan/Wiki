#!/bin/sh

a=0

while [ $a -lt 1000 ]
do
   echo $a
   a=`expr $a + 1`
   wget http://cs231n.stanford.edu/reports/2017/posters/$a.pdf
done
