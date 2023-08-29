import os
import subprocess

# Read the requirements.txt file and get the list of required packages
with open('requirements.txt', 'r') as f:
    required_packages = f.readlines()

# Remove any extra whitespace or newline characters
required_packages = [pkg.strip() for pkg in required_packages]

# Get the list of all installed packages using pip freeze
installed_packages = subprocess.getoutput('pip freeze')
installed_packages = installed_packages.split('\n')

# Extract just the package names
installed_packages = [pkg.split('==')[0] for pkg in installed_packages]

# Find packages that are installed but not required
unwanted_packages = set(installed_packages) - set(required_packages)

# Uninstall unwanted packages
for pkg in unwanted_packages:
    print(f'Uninstalling {pkg}...')
    os.system(f'pip uninstall -y {pkg}')

print('Cleanup complete.')