import sys
import subprocess

# Auto installing the required package:
#subprocess.check_call([sys.executable, 'get-pip.py'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyperclip'])


input("All Done! Press q to exit\n")