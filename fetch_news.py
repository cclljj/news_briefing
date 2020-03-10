#!/usr/bin/env python

import argparse
import requests
import json
from datetime import date

URL_everything = "http://newsapi.org/v2/everything"

today = date.today()
today = today.strftime("%Y%m%d")

def fetch_news(KEY, TOPIC, PREFIX):
	results = {}
	headers = {}
	OUT = PREFIX + "/out-" + today + ".json"
	with open(KEY, 'r') as keyfile , open(TOPIC, 'r') as topicfile, open(OUT, 'w') as outfile:
		KEY = keyfile.readline()
		KEY = KEY.strip()
		keyfile.close()
		headers['X-Api-Key'] = KEY

		for topic in topicfile:
			topic = topic.strip()
			r = requests.get(URL_everything + "?q=" + topic, headers=headers)
			results[topic] = r.content

		json.dump(results, outfile)

		


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Retrieve data of one specific project on a specific date')
	parser.add_argument("-k", dest="KEY", type=str, help="NewsAPI key", required=True)
	parser.add_argument("-t", dest="TOPIC", type=str, help="Topic list file (*.txt)", required=True)
	parser.add_argument("-p", dest="PREFIX", default="/tmp", type=str, help="Output folder (default: /tmp)")
	args = parser.parse_args()

	fetch_news(args.KEY, args.TOPIC, args.PREFIX)
