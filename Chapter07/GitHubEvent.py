#Github Events list public activities that have been performed within the past 90 days.
#These events are provided in pages, with 30 items per page and a maximum of 300 being
#shown.

import requests
import json
from collections import Counter
dataSet = []

url = 'https://api.github.com/'
#If you’d like to add HTTP headers to a request, simply pass in a dict
#to the headers parameter

headers = {'Accept':'application/vnd.github.v3.full+json'}

def readUrl(search):
    results = requests.get(url + search, headers=headers)
    print("Status Code: ", results.status_code)
    print("Headers: Content-Type: ", results.headers['Content-Type'])
    return results.json()


if __name__ == "__main__":
    eventTypes=[]
    #IssueCommentEvent,WatchEvent,PullRequestReviewCommentEvent,CreateEvent
    for page in range(1, 4):
        events = readUrl('events?page=' + str(page))
        # print(jsonResult)
        for event in events:
            id = event['id']
            type = event['type']
            actor = event['actor']['display_login']
            repoUrl = event['repo']['url']
            createdAt = event['created_at']
            eventTypes.append(type)
            dataSet.append([id, type, createdAt, repoUrl, actor])

    eventInfo = dict(Counter(eventTypes))
    print("Individual Event Counts:", eventInfo)
    print("CreateEvent Counts:", eventInfo['CreateEvent'])
    print("DeleteEvent Counts:", eventInfo['DeleteEvent'])

print("Total Events Found: ", len(dataSet))
print(dataSet)
