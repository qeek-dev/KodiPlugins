import time
import xbmc
import sys
import subprocess
import xbmcaddon
import xbmcgui
__addon__ = xbmcaddon.Addon()

header = "ZFS Check"

def run():
    cmd = "zpool status"
    process = subprocess.Popen(cmd, shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    out, err = process.communicate()
    errcode = process.returncode
    return str(out)


def text_viewer(title, text):
    WINDOW = 10147 # Text Viewer window in XBMC
    TITLEBAR = 1
    CONTENTS = 5
    xbmc.executebuiltin("ActivateWindow(%d)" % WINDOW)
    w = xbmcgui.Window(WINDOW)
    xbmc.sleep(500)
    w.getControl(TITLEBAR).setLabel(title)
    w.getControl(CONTENTS).setText(text)

if __name__ == '__main__':
    text_viewer(header,run())
