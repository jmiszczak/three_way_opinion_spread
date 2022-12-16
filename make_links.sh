#!/bin/bash
for sn in `cat experiments.xml | grep -Po "(?<=name=\")[_a-z0-9-]*" `; do 
  echo "[INFO] Creating link for experiment $sn"
	ln -sf ./run.sh $sn.sh
  chmod +x $sn.sh
done
