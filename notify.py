import win10
import win11
import get_os
import sys

if get_os.os == 'Windows':
    if get_os.os_version == '10':
        win10.win10()
    elif get_os.os_version == '11':
        win11.win11()
    else:
        sys.exit()
else:
    print("This script can only be run under Windows!")
    sys.exit()
