[![Open Code Badge](https://www.comses.net/static/images/icons/open-code-badge.png)](https://www.comses.net/codebases/42c95a84-ca79-4d71-91e0-12ac436e9673/releases/1.0.0/)

# three_way_opinion_spread

Implementation and description of experiments for three-way opinion spread
model based on the three channels of virus propagation.

## Files

The repository contains the following files:
  - `v3w.netlogo` - model in NetLogo (version 6.2.1)
  - `expName-expDesc.sh` - files for running headless NetLogo experiment,
  - `expName.csv` - files with data obtained from *expName* experiment, created after running
    the experiment
  - `expName-*.py` - plotter files for data from *expName*, which might be based on data
    from several experiments.

**Note**:  
  - All experiments were executed on Linux machines (Ubuntu 20.04 or 22.04),
  - To run scripts controlling the experiments `netlogo-headless.sh` must be in
    your $PATH.
  - Model can be also obtained from Modeling Commons at 
http://www.modelingcommons.org/browse/one_model/6946
## Experiments

### **exp1** and **exp2**

**Goal**: Observer the dynamics of infection/opinion for selection of mobility
and patch contamination probabilities.

Experiments **exp1x** and **exp2x** have different patch healing probability
comparing to **exp1** and **exp2**.

  - Description: interplay between mobility, patch contamination, and patch infection weight.
  - Time limit: 5000
  - Repetitions: 50
  - World:
     - population: 250,
     - grid: 33x33, 
     - obstacles: 10% of the grid, 
     - initial contamination: 10% of the grid, 
     - initially infected agents: 5% of the population, 
     - direct infection weight: 0.25
     - indirect infection: w_2 = 1-(w_1+w_3)
  - Healing params (healing with some p at each step)
    - healing prob for agent: 0.25, 
    - healing prob for patch 0.05
  - Variables: 
    - mobility (0..1), 
    - patch contamination (0..1),
    - patch infection weight (0..1),
  - Reporters: 
    - %infected, 


### **exp3**, **exp4**, **exp5**, and **exp6**

**Goal**: Provide examples of opinion dynamics with various scenarios of the
weights assignments.

  - **exp3**: w1=w2=w3=1/3
  - **exp4**: w1=w2=1/4, w3=1/2
  - **exp5**: w1=2/3, w2=2. w3=1/3
  - **exp6**: w1=2/3, w2=1/3, w3=0
  
