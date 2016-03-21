from xml.dom.minidom import parse
from functions import launch_scraper, create_opener

try:
    config = parse("config.xml").getElementsByTagName("single_video_search")[0]
    opener = create_opener()

    for singleVideo in config.getElementsByTagName("video"):
        video_id = singleVideo.getAttribute("id")
        stats = launch_scraper(video_id, create_opener())
        print "stats: ", stats

except KeyboardInterrupt:
    pass
except Exception as exc:
    print "Error: ", exc
