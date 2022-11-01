<a href="https://www.comses.net/codebases/42c95a84-ca79-4d71-91e0-12ac436e9673/releases/1.1.0/">
  <img height="100" src="https://www.comses.net/static/images/icons/open-code-badge.png" alt="Open Code Badge">
</a>



[![DOI](https://zenodo.org/badge/465858115.svg)](https://zenodo.org/badge/latestdoi/465858115)


# three_way_opinion_spread

Implementation and description of experiments for three-way opinion spread
model based on the three channels of virus propagation.

## Files

The repository contains the following files:
  - `v3w.netlogo` - model in NetLogo (tested with version 6.2.1)
  - `run.sh` - cotroller for running the experiements, it will run the apopriate
    experiements from `experiments.xml` (see below,
  - `make_links.sh` - script for creating symbolik links for running headless NetLogo experiments,
  - `expName.csv` - files with data obtained from *expName* experiment, created after running
    the experiment
  - `expName-*.py` - plotter files for data from *expName*, which might be based on data
    from several experiments.

**Note**:  
  - All experiments were executed on Linux machines (Ubuntu 20.04 or 22.04),
  - To run scripts controlling the experiments `netlogo-headless.sh` must be in
    your $PATH.
  - Model can be also obtained from Modeling Commons at http://www.modelingcommons.org/browse/one_model/6946

## How to run the code?

To run one of the experiements described in `experiements.xml`, execute
`make_links.sh` script. It will result in a number of symbolic links,
corresponding to the sections of XML file describing the experiments. Running
any of the scripts will start the corresponding experiement,  eg.

  ```./exp7-realizations.sh```
