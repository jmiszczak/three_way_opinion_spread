# three_way_opinion_spread
Implementation and description of experiments for three-way opinion spread

## Files
- ```v3w.netlogo``` - model in NetLogo 
- expName-expDesc.sh - file for running headless NetLogo experiment,
- expName-expDesc.py - plotter for data from *expName*,
- expName.csv - data obtained from *expName* experiment,
- ```pack.sh``` and ```unpack.sh``` - scripts for compressing/uncompressing resulting data.

## Experiments

### **exp1** and **exp2**
**Goal**: Observer the dynamics of infection/opinion for selection of params.

First two experiements differ only in the infection probability (1 in exp1 and
0.5 in exp2).

  - Description: interplay between mobility, patch contamination, and patch infection weight.
  - Time limit: 5000
  - Repetitions: 20
  - World:
     - population: 250,
     - grid: 33x33, 
     - obstacles: 10% of the grid, 
     - initial contamintaion: 10% of the grid, 
     - initially infected agents: 5% of the population, 
     - direct infection weight: 0.25
     - indirect infection: w_2 = 1-(w_1+w_3)
  - Healing params (healing with some p at each step)
    - healing prob for agent: 0.25, 
    - healing prob for patch 0.05
  - Vaiables: 
    - mobility (0..1), 
    - patch contamination (0..1),
    - patch infection weight (0..1),
  - Reporters: 
    - %infected, 


### **exp3** and **exp4**

**Goal**:Examples of realizations with w1=w2=w3=1/3 and w1=w3=1/2, w2=0  

**Note**: all experiments are distributed XML files

