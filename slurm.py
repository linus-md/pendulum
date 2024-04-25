import os
import sys
import datetime
import subprocess

def create_and_run_sh(filename):
    time = datetime.datetime.now().strftime("%M%S")
    script_path = f'slurm_{time}.sh'
 
    script_content = f"""#!/bin/bash --login
#SBATCH --job-name={filename.split('/')[-1][:-3]}_{time}
#SBATCH --output=logs/{filename.split('/')[-1][:-3]}_{time}.out
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=64GB
#SBATCH --time=7-0:00
mamba activate sage
export PYTHONPATH="${{PYTHONPATH}}:/home/mathexp/lsommer/code/pendulum"
time python {filename}
"""

    with open(script_path, 'w') as script_file:
        script_file.write(script_content)

    full_script_path = os.path.abspath(script_path)
    os.chmod(script_path, 0o755)

    try:
        print("Executing the script...")
        subprocess.run(['sbatch', full_script_path], check=True)
        print("Job submitted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Script failed with exit code {e.returncode}")
    finally:
        os.remove(full_script_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python slurm.py <folder.filename>")
        sys.exit(1)

    filename = sys.argv[1]
    create_and_run_sh(filename)
