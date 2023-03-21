import time

from .Config import *
from .core import *
from .Resources import *

start_time = time.time()
# Sudo Users
sudos = []
# full debugging
if SUDO_USERS:
    try:
        sudouser = SUDO_USERS
        print(sudouser)
        _list = [int(x) for x in sudouser]
        sudos = _list
    except Exception as e:
        sudos = SUDO_USERS
        print(e)
else:
    print("Add Key Sudo User")
