
import re
import urllib2
import xbmc
import xbmcaddon
import xbmcgui
import xml.dom.minidom as dom

def log(info):
    print '[############] %s'%repr(info)

log('Starting MVG Checker')

__addon__ = xbmcaddon.Addon()


def getSetting(setting_id):
    """Workaround because __addon__.getSetting returns '' alltime"""
    __addon__ = xbmcaddon.Addon()
    __addonid__    = __addon__.getAddonInfo('id')
    __configfilepath__ = xbmc.translatePath("special://profile/addon_data/" + __addonid__ + '/settings.xml')
    try:
        root = dom.parse(__configfilepath__)
        sets = root.getElementsByTagName("setting")
        for setting in sets:
            if setting.getAttribute("id") == setting_id:
                return setting.getAttribute("value")
        return ""
    except:
        return ""

class MVG:

    """This Library gives MVG Departments fom any destination
    Thanks to pc-coholic: <fpletz@phidev.org>"""

    def encode_station_name(self, stationname):
        string = urllib2.quote(stationname.encode('latin1'))
        return string

    def get_departures(self, station, mintime=1,maxtime = 20):
        log('Station: %s'%station)
        log('Mintime: %s'%mintime)
        log('Maxtime: %s'%maxtime)

        mintime = int(mintime)
        maxtime = int(maxtime)
        enc_station = self.encode_station_name(station)

        REGEXP = re.compile(r'<tr class="[^"]+">'+
        '<td class="lineColumn">(\w+)</td>'+
        '<td class="stationColumn">([^<]+)<span class="spacer">&nbsp;</span>'+
        '</td><td class="inMinColumn">(\d+)')

        url = 'http://www.mvg-live.de/ims/dfiStaticAnzeige.svc?haltestelle=%s'%enc_station
        log('URL: %s'%repr(url))
        counter = 0
        while counter < 3:
            counter += 1
            try:
                s = urllib2.urlopen(url).read().replace('\r\n', '').replace('\t', '').decode('ISO-8859-1')
            except:
                pass
        d = REGEXP.findall(s)
        outlist = []
        if len(d) == 0:
            return None
        else:
            for (line, dest, t) in d:
                if int(t) <= maxtime and int(t) >= mintime:
                    outlist.append('%2s Minutes: %s %-24s' % (t,line, dest))
            outlist.sort()
            return outlist

def text_viewer(title, text):
    WINDOW = 10147 # Text Viewer window in XBMC
    TITLEBAR = 1
    CONTENTS = 5
    xbmc.executebuiltin("ActivateWindow(%d)" % WINDOW)
    w = xbmcgui.Window(WINDOW)
    xbmc.sleep(500)
    w.getControl(TITLEBAR).setLabel(title)
    w.getControl(CONTENTS).setText(text)


# Get Settings
station = getSetting('station')
mintime = getSetting('mintime')
if mintime == '':
    mintime = 1
maxtime = getSetting('maxtime')
if maxtime == '':
    maxtime = 100

# Wrong Time Settings?
if int(mintime) >= int(maxtime):
    mintime = 1
    maxtime = 30
    __addon__.setSetting(id="mintime",value='1')
    __addon__.setSetting(id="maxtime",value='30')


# Wrong Station in Settings
mvg_obj = MVG()
data = mvg_obj.get_departures(station)
if not data:
    station = ''

if station == '':
    # No usable Station found
    while 1:
        kb = xbmc.Keyboard(heading='Station')
        kb.doModal()
        if (kb.isConfirmed()):
            # Station Confirmed
            station = kb.getText().decode('utf-8')
            log('Trying: %s'%station)

            data = mvg_obj.get_departures(station)
            if not data:
                log('Got No Data: %s'%station)
                continue
            else:
                log('Save: %s'%station)
                __addon__.setSetting(id="station",value=station)
                break
        else:
            # Cancelled
            exit(0)

# Show Depart Infos
log('Showing Output: %s'%station)
data = mvg_obj.get_departures(station,mintime,maxtime)
info = ''
for line in data:
    info += line + '\n'
text_viewer(station,info)


