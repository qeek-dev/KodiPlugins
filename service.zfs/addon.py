import time
import xbmc
import sys
import subprocess


sleeptime = 100
timeout = 20
header = "ZFS Check"


def run():
    cmd = "zpool status -x"
    process = subprocess.Popen(cmd, shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    out, err = process.communicate()
    errcode = process.returncode
    return str("%s%s Code(%s)"%(out, err, errcode)).replace('\n','')

if __name__ == '__main__':
    monitor = xbmc.Monitor()

    try:
        subprocess.call(['zpool'])
    except:
        xbmc.executebuiltin("Notification (%s ,%s, %d)"%(header,'Error: ZFS not installed!',timeout))
        sys.exit(0)

    info = run().replace('\\n','')    
    xbmc.executebuiltin("Notification (%s ,%s, %d)"%(header,info,timeout))

    while True:
        if monitor.waitForAbort(sleeptime):
            break

        if not xbmc.Player().isPlaying():
            info = run()
            xbmc.executebuiltin("Notification (%s ,%s, %d)"%(header,info,timeout))


