import os
import subprocess

def get_train_results(source, dest):
    os.makedirs(dest, exist_ok=True)
    subprocess.run(f'mv {source} {dest}', shell=True)
    subprocess.run(f'rm -rf ./runs', shell=True)