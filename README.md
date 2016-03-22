YOUStatAnalyzer
===============

YOUStatAnalyzer is a tool written in Python able to capture the popularity metrics of YouTube's videos. Since in June 2013 YouTube removed the API that allowed to retrieve the statistics available below each video, we needed to find a new way of obtain those kind of data. The result is this piece of software that allows to automatically and in a fast way to download YouTube's videos statistics with the final purpose of creating a dataset for analysis. In order to extract these data from YouTube, the tool obtains a session token that is later used for making the request to YouTube's servers.

## Usage

1. Install the requirements from the `requirements.txt` file.
2. Start Flask website locally by typing `python app.py`.
3. Enter the ID of a YouTube video (e.g. `3HuYr6G2Z28` from the video link: `https://www.youtube.com/watch?v=3HuYr6G2Z28`)

Some videos don't have statistics available, such as official movie trailers of newer movies.