import time
import xbmc
import sys
import subprocess
import xbmcaddon
__addon__ = xbmcaddon.Addon()

header = "ZFS Check"

def getSetting(setting_id):
    """Workaround because __addon__.getSetting returns '' alltime"""

    import xml.dom.minidom as dom
    __addon__ = xbmcaddon.Addon()
    __addonid__    = __addon__.getAddonInfo('id')
    __configfilepath__ = xbmc.translatePath("special://profile/addon_data/" + __addonid__ + '/settings.xml')
    print 'Opening Configfile: %s'%__configfilepath__
    try:
        root = dom.parse(__configfilepath__)
        sets = root.getElementsByTagName("setting")
        for setting in sets:
            print setting.getAttribute("id"), setting.getAttribute("value")
            if setting.getAttribute("id") == setting_id:
                return setting.getAttribute("value")
        return ""
    except Exception,e:
        print str(e)
        return ""


disabled = getSetting("zfs.disabled")

if disabled == 'true':
    exit(0)

try:
    timeout = int(getSetting("zfs.timeout"))*1000
    sleeptime = int(getSetting("zfs.sleeptime"))
except:
    __addon__.setSetting(id="zfs.disabled",value='false')
    __addon__.setSetting(id="zfs.timeout",value='5')
    __addon__.setSetting(id="zfs.sleeptime",value='100')
    timeout = 5*1000
    sleeptime = 100


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
        timeout = int(__addon__.getSetting("zfs.timeout"))*1000
        sleeptime = int(__addon__.getSetting("zfs.sleeptime"))

        if monitor.waitForAbort(sleeptime):
            break

        while xbmc.Player().isPlaying():
            monitor.waitForAbort(1)


        info = run()
        xbmc.executebuiltin("Notification (%s ,%s, %d)"%(header,info,timeout))
