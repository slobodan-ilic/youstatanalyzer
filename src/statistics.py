# _*_ coding: utf-8

from functions import launch_scraper, create_opener
import xlsxwriter
from cStringIO import StringIO


def analyze_stats(video_id):
    try:
        stats = launch_scraper(video_id, create_opener())
        return stats
    except Exception as exc:
        print "Error : ", exc


def generate_spreadsheet(stats, filename):
    if 'day' in stats.keys():
        output = StringIO()
        # wb = xlsxwriter.Workbook(output, {'in_memory': True})
        wb = xlsxwriter.Workbook(filename)
        ws = wb.add_worksheet('Stats')
        # Create title
        ws.write(0, 0, 'Video')
        ws.write(0, 1, stats['title'].decode('utf-8'))
        # Create headers
        ws.write(2, 0, 'Day')
        ws.write(2, 1, 'Cumulative Views')
        ws.write(2, 2, 'Daily Views')
        ws.write(2, 3, 'Cumulative Shares')
        ws.write(2, 4, 'Daily Shares')
        # Write data
        start = 4
        for i in range(len(stats['day']['data'])):
            ws.write(start + i, 0, stats['day']['data'][i])
            ws.write(start + i, 1, stats['views']['cumulative']['data'][i])
            ws.write(start + i, 2, stats['views']['daily']['data'][i])
            ws.write(start + i, 3, stats['shares']['cumulative']['data'][i])
            ws.write(start + i, 4, stats['shares']['daily']['data'][i])
        wb.close()
        # return output
