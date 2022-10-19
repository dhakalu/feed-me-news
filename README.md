# feed-me-news

This is a python program that reads news from different RSS feeds and displays them.

[ ] A lambda function is ran every 15 min to update the feed.
[ ] Lambda function filters the news published after the last scanned time.
[ ] Then it saves the new posts to the s3 as json file
[ ] S3 has an event trigger that calls the lambda function to apply tags
