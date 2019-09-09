# SessionSetup.py
# Robert Grupe, 2019-09-08

import subprocess

def check_versions():
    nodeVersion = subprocess.Popen(['node', '-v'], 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT,
        universal_newlines=True)                  # Needed to strip off extra pre and post formatting characters
    stdout, stderr = nodeVersion.communicate()
    nodeVersion_status = nodeVersion.wait()

    print('\n Currently installed Node.JS version is: ', stdout)
    return

check_versions()

# TODO npmVersion = ["npm", "-v"]
# TODO compare to latest published version
# TODO Error Handling: install if missing to install -https://nodejs.org/en
# TODO Update to latest version of npm and node.js
# sudo npm cache clean -f
# sudo npm install -g n
# sudo n stable
# Reference: https://askubuntu.com/questions/155791/how-do-i-sudo-a-command-in-a-script-without-being-asked-for-a-password