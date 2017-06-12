import sys
import re
import routing
import xbmcaddon
import xbmcgui
import xbmcplugin
from xbmcgui import ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory
import CommonFunctions as xbmc_common
# from resources.lib import kodiutils
# from resources.lib import kodilogging
# from xbmcgui import ListItem
# from xbmcplugin import addDirectoryItem, endOfDirectory
# 
# # 


# # 
# # import routing

# 
def getVideoUrl(articleUrl):
    articleHTML = xbmc_common.fetchPage({"link": articleUrl})
    regex = r"href=\"(.+?mp4)\""
    content = articleHTML['content']
    matches = re.finditer(regex, content)
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            return content[match.start(groupNum):match.end(groupNum)]
    return ''
    
def getCategory(category):
    categoryHTML = xbmc_common.fetchPage({"link": "https://sub.media/c/" + category + "/"})
    category = xbmc_common.parseDOM(categoryHTML['content'], 'main', attrs = {'id': 'main'})
    articles = xbmc_common.parseDOM(category, 'article')
    
    for article in articles:
        img = xbmc_common.parseDOM(article, 'img', ret = 'src')
        title = xbmc_common.parseDOM(article, 'a', ret = 'title')
        articleUrl = xbmc_common.parseDOM(article, 'a', ret = 'ref')
        desc = xbmc_common.parseDOM(article, 'p')
        
        urlVideo = getVideoUrl(articleUrl[0])
        
        # print title[0].encode('utf-8')
        # print urlVideo
        if len(urlVideo) > 0:
            li = xbmcgui.ListItem(title[0].encode('utf-8'), iconImage=img[0])
            addDirectoryItem(handle=plugin.handle, url=urlVideo, listitem=li)
        else:
            #http://kodi.wiki/view/Add-on:YouTube
            print title[0].encode('utf-8')
            print urlVideo
            print "failed"

plugin = routing.Plugin()

@plugin.route('/')
def index():
    addDirectoryItem(plugin.handle, plugin.url_for(show_category, "trouble"), ListItem("Trouble"), True)
    addDirectoryItem(plugin.handle, plugin.url_for(show_category, "stimulator"), ListItem("Stimulator"), True)
    addDirectoryItem(plugin.handle, plugin.url_for(show_category, "a-is-for-anarchy"), ListItem("A is for Anarchy"), True)
    addDirectoryItem(plugin.handle, plugin.url_for(show_category, "video-ninjas"), ListItem("Video Ninjas"), True)
    addDirectoryItem(plugin.handle, plugin.url_for(show_category, "submedia-films"), ListItem("Submedia Films"), True)
    addDirectoryItem(plugin.handle, plugin.url_for(show_category, "featured-content"), ListItem("Featured Content"), True)
    addDirectoryItem(plugin.handle, plugin.url_for(show_category, "collaborations"), ListItem("Collaborations"), True)
    endOfDirectory(plugin.handle)

@plugin.route('/category/<category_id>')
def show_category(category_id):
    getCategory(category_id)
    endOfDirectory(plugin.handle)

if __name__ == '__main__':
    plugin.run()