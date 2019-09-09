# SessionSetup.py
# Contributors: Robert Grupe
# Version: 2019-09-09

import subprocess

def this_platform():
    # TODO https://stackoverflow.com/questions/110362/how-can-i-find-the-current-os-in-python
    return

def check_version (tool, command, option):
    nodeVersion = subprocess.Popen([command, option], 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT,
        universal_newlines=True)                  # Needed to strip off extra pre and post formatting characters
    stdout, stderr = nodeVersion.communicate()
    nodeVersion_status = nodeVersion.wait()

    print('\n Currently installed', tool, 'version is: ', stdout)
    return

this_platform()
check_version('Node.JS','node', '-v')
check_version('nmp','npm', '-v')

# TODO add test for function
# TODO compare to latest published version
# TODO Error Handling: install if missing to install -https://nodejs.org/en
# TODO Update to latest version of npm and node.js
# sudo npm cache clean -f
# sudo npm install -g n
# sudo n stable
# Reference: https://askubuntu.com/questions/155791/how-do-i-sudo-a-command-in-a-script-without-being-asked-for-a-password