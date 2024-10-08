# python3 -m venv venv_name => create a new venv
# source venv_name/bin/activate => activate the venv
# deactivate => deactivate the venv
# pip list => list the installed packages in the current environment along with their versions
# which python => show what python is used (the path of the used python)

# pip freeze => list the installed packages in the current environment along with their versions in a 'package==version' format 
#               that can be used to create a 'requirements.txt' file, which can be used to replicate the environment
# pip freeze > requirements.txt => create a file contain the pip freeze command output
# pip install -r requirements.txt => install the 'requirements.txt' file content
