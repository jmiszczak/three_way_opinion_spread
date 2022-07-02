#!/bin/bash
expName=${0/.sh/}
expName=${expName/./}
expName=${expName/\//}
echo "[INFO] Running experiment: " $expName
echo -n "[INFO] Start time: "
date +"%H:%M"
netlogo-headless.sh --threads 16 --model v3w.nlogo --setup-file experiments.xml --table $expName.csv --experiment $expName
echo -n "[INFO] End time:"
date +"%H:%M"

