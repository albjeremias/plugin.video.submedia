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
import re
import xbmcgui
import xbmcplugin
import CommonFunctions as xbmc_common

def getVideoUrl(articleUrl):
    print articleUrl
    articleHTML = xbmc_common.fetchPage({"link": articleUrl})
    regex = r"href=\"(.+?mp4)\""
    content = articleHTML['content']
    matches = re.finditer(regex, content)
    # content[match.start(groupNum):match.end(groupNum)]
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            print content[match.start(groupNum):match.end(groupNum)]
            return content[match.start(groupNum):match.end(groupNum)]
    return ''
    
def getCategory(category):
    categoryHTML = xbmc_common.fetchPage({"link": "https://sub.media/c/" + category + "/"})
    # print repr(result['content'])
    category = xbmc_common.parseDOM(categoryHTML['content'], 'main', attrs = {'id': 'main'})
    articles = xbmc_common.parseDOM(category, 'article')
    
    for article in articles:
        img = xbmc_common.parseDOM(article, 'img', ret = 'src')
        title = xbmc_common.parseDOM(article, 'a', ret = 'title')
        articleUrl = xbmc_common.parseDOM(article, 'a', ret = 'ref')
        desc = xbmc_common.parseDOM(article, 'p')
        print repr(title)
        print repr(desc)
        print repr(img)
        
        urlVideo = getVideoUrl(articleUrl[0])
        print "video ::: "
        print urlVideo
        # url = 'https://archive.org/download/FlagBurn/HowToBurnAnAmericanFlag720p.mp4'
        li = xbmcgui.ListItem(title[0].encode('utf-8'), iconImage='DefaultVideo.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=urlVideo, listitem=li)
        # print repr(ret[0])

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

getCategory("trouble")



xbmcplugin.endOfDirectory(addon_handle)


