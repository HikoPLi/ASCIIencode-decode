import platform
# function
import macOSInfo
import windowsInfo


def platForm():

    if platform.system().lower() == 'Windows':


        str = windowsInfo.info()

        return str

    if platform.system().lower() == 'darwin':

        str = macOSInfo.info()

        return str
