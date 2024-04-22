#!/bin/bash --login
#SBATCH --job-name=systems/pendulum/single.py_3803
#SBATCH --output=logs/systems/pendulum/single.py_3803.out
mamba activate sage
time python systems/pendulum/single.py
