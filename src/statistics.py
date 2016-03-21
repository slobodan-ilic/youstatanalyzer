from functions import launch_scraper, create_opener


def analyze_stats(video_id):
    try:
        stats = launch_scraper(video_id, create_opener())
        return stats
    except Exception as exc:
        print "Error : ", exc
