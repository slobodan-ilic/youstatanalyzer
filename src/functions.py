import urllib2
import cookielib
import re

HOST = 'www.youtube.com'
GDATA_HOST = 'gdata.youtube.com'
TOKEN_KEYWORD = 'account_playback_token'
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) '
      'AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/31.0.1650.57 Safari/537.36')

config_file = "config.xml"


def yt_video_url(vid): return 'http://%s/watch?v=%s' % (HOST, vid)


def yt_insights_url(vid): return 'https://%s/insight_ajax?action_get_statistics_and_data=1&v=%s' % (HOST, vid)


def create_opener(cookie_jar=None):
    if not cookie_jar:
        cookie_jar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
    opener.addheaders = [('User-Agent', UA)]
    return opener


def fetch_video_html(opener, video_id):
    stream = opener.open(yt_video_url(video_id))
    html = stream.read()
    stream.close()
    return html


def fetch_video_insights(opener, video_id, token):
    url = yt_insights_url(video_id)
    data = 'session_token=%s' % token
    headers = {
        'Origin': 'http://%s' % HOST,
        'Referer': yt_video_url(video_id)
    }
    req = urllib2.Request(url, data, headers, HOST)
    stream = opener.open(req)
    return stream.read()


def get_insight_ajax_token(html):
    m = re.search('\"'+TOKEN_KEYWORD+'\":\"(.+?)\"', html)
    if m:
        return m.group(1)


def get_video_title(html):
    search_pattern = '(?<=<title>).*(?=</title>)'
    m = re.search(search_pattern, html)
    if m:
        return m.group(0)


def extract_video_statistics (vid_id, title, data):
    stats_data = [map(float, elem.split(',')) for elem in re.findall(r'["]+[\w]+[\\":]+[ ]+[\[]+([\d\.\d,\s]+|[\d,\s]+|[\d,\s\d]+|[-\d\.\d,\s]+|[-\d,\s]+|[-\d,\s\d]+)+[\]]', data)]
    stats_labels = re.findall(r'["]+[views]+[\\":]+|["]+[shares]+[\\":]+|["]+[subscribers]+[\\":]+|["]+[day]+[\\":]+|["]+[cumulative]+[\\":]+|["]+[daily]+[\\":]+|["]+[watch\-time]+[\\":]+', data)
    stats = ['views', 'shares', 'subscribers', 'watch-time']
    stat_types = ['cumulative', 'daily']

    video_data = {
        'title': title,
        'vid_id': vid_id
    }

    ii = 0
    level1 = None
    level2 = None
    for label in stats_labels:
        label = label.strip('":')
        if label in stats:
            level1 = label
            video_data[level1] = {}
        elif label in stat_types:
            level2 = label
            video_data[level1][level2] = {}
            video_data[level1][level2]["data"] = stats_data[ii]
            ii += 1
        elif label == 'day':
            level1 = label
            video_data[level1] = {}
            video_data[level1]["data"] = stats_data[ii]
            ii += 1

    return video_data


def launch_scraper(vid_id, opener):
    video_page = fetch_video_html(opener, vid_id)
    token = get_insight_ajax_token(video_page)
    title = get_video_title(video_page)

    print "Video id: {0}".format(vid_id)
    print "Title: {0}".format(title)

    if not token:
        print "No session token"
        raise ValueError("Couldn't find session_token in %s" % video_page)

    data = fetch_video_insights(opener, vid_id, token)

    if '"data":' in data:
        return extract_video_statistics(vid_id, title, data)
    else:
        raise Exception("No statistics available for this video.")
