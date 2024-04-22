#!/bin/bash --login
#SBATCH --job-name=systems/pendulum/single.py_3720
#SBATCH --output=logs/systems/pendulum/single.py_3720.out
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=16GB
#SBATCH --time=1-0
mamba activate sage
time python systems/pendulum/single.py
