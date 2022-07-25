#!/bin/bash
for sn in `cat experiments.xml | grep -Po "(?<=name=\")[_a-z0-9-]*" `; do 
	ln -s ./run.sh $i.sh ;
done
