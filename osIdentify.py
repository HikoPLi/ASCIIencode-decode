import platform
# function
import macOSInfo


def platForm():

    if platform.system().lower() == 'Windows':

        import windowsInfo

        str = windowsInfo.info()

        return str

    if platform.system().lower() == 'darwin':

        str = macOSInfo.info()

        return str
