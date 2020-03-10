# news_briefing

## Goal
1. use NewsAPI (https://newsapi.org) to fetch news of interests into a JSON file
2. use d3.js to display the JSON content in Collapsible Tree (https://observablehq.com/@d3/collapsible-tree)

## Note

To use this program, you need to apply for an API key from NewsAPI (https://newsapi.org) in advance. NewsAPI is offering free API key for individual deveopers. If you are using NewsAPI for commercial purpose, you should contact NewsAPI for pricing information.

## Example:

```
usage: fetch_news.py [-h] -k KEY -t TOPIC [-p PREFIX]
```

```
python fetch_news.py -k .key -t topic.txt -p /tmp
```

