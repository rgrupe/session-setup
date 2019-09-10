""" SessionSetup.py: Automates the installation and updating of development tools after login.
    Contributors: Robert Grupe
    Version: 2019-09-09
"""

import platform
import subprocess

def this_host():
    """  Return host system operating system name. """
    host_os = platform.system()
    print('This platform OS is: ', host_os)
    return

def check_version (tool, command, option):
    """ Run OS shell command and return results. """
    response = subprocess.Popen([command, option], 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT,
        universal_newlines=True)                  # Needed to strip off extra pre and post formatting characters
    stdout, stderr = response.communicate()
    response_status = response.wait()

    print('Currently installed', tool, 'version: ', stdout)
    return

this_host()
check_version('Node.JS','node', '-v')
check_version('nmp','npm', '-v')

# TODO add functions unit tests
# TODO compare to latest published version
# TODO Error Handling: install if missing to install -https://nodejs.org/en
# TODO Update to latest version of npm and node.js
# sudo npm cache clean -f
# sudo npm install -g n
# sudo n stable
# Reference: https://askubuntu.com/questions/155791/how-do-i-sudo-a-command-in-a-script-without-being-asked-for-a-password