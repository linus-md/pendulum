#!/bin/bash --login
#SBATCH --job-name=systems/kepler/kepler_simple_2720
#SBATCH --output=logs/systems/kepler/kepler_simple_2720.out
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=16GB
#SBATCH --time=1-00:00:00
mamba activate sage
time python systems/kepler/kepler_simple
