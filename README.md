# session-setup
This application is a script to automate personal workstation development tools setup.
1. Install missing tools
1. Update tools to latest versions

## Status
**Unstable**: This project is currently being actively designed and developed.

## Use
1. Pre-requisite: python 3.5+ installed.  
``` $ python3 -V```
1. Add this application to your login start programs.
```$ python3 session-setup.py```

## Features
* 000 Python3 for platform portability.
* 001 Start local server: node
* 002 Check for developement tools, and install or update as needed:
*   002.1 npm and Node.JS
*    002.2 pip and Python3
*   002.3 IDEs
*      002.3.1 vim
*      002.3.2 Visual Studio Code
* 003 Delete temporary files: weekly Temp folder, daily duplicate backup files
* 004 Backup data files: weekly full, daily incremental
* ß005 Auto detect environment to update MacOS or Windows