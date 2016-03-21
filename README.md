YOUStatAnalyzer
===============

YOUStatAnalyzer is a tool written in Python able to capture the popularity metrics of YouTube's videos. Since in June 2013 YouTube removed the API that allowed to retrieve the statistics available below each video, we needed to find a new way of obtain those kind of data. The result is this piece of software that allows to automatically and in a fast way to download YouTube's videos statistics with the final purpose of creating a dataset for analysis. In order to extract these data from YouTube, the tool obtains a session token that is later used for making the request to YouTube's servers.

## Usage

Start Flask website locally. Use by entering ID of the video to be analyzed.

To run the web server use the command: ```python app.py``` The website will be available at localhost.
