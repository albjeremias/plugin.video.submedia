# -*- coding: utf-8 -*-
# 
# from resources.lib import kodilogging
# from resources.lib import plugin
# 
# import logging
# import xbmcaddon
# 
# # Keep this file to a minimum, as Kodi
# # doesn't keep a compiled copy of this
# ADDON = xbmcaddon.Addon()
# kodilogging.config()
# 
# plugin.run()

import sys
import xbmcgui
import xbmcplugin
import CommonFunctions
import urllib2

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

# common = CommonFunctions
# common.plugin = "Submedia Kodi v1.0"
# 
urllib2.urlopen('http://sub.media')

url = 'https://archive.org/download/FlagBurn/HowToBurnAnAmericanFlag720p.mp4'
li = xbmcgui.ListItem('My Second Video!', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
