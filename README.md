YOUStatAnalyzer
===============

YOUStatAnalyzer is a tool written in Python able to capture the popularity metrics of YouTube's videos. Since in June 2013 YouTube removed the API that allowed to retrieve the statistics available below each video, we needed to find a new way of obtain those kind of data. The result is this piece of software that allows to automatically and in a fast way to download YouTube's videos statistics with the final purpose of creating a dataset for analysis. In order to extract these data from YouTube, the tool obtains a session token that is later used for making the request to YouTube's servers.

## Usage

The software is very easy to use, just need to configure it and run.

To run it use the command: ```python youtube_script.py config.xml``` where config.xml is of course the configuration file. The tool will automatically read it and react accordingly.
