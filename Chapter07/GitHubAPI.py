# In this example the objective is to reveal the cache property of the
# RESTful API. It is considered one of the most important properties of
# RESTful web services. This helps with processing time as well as bandwith
# time and usage.

import requests

url = 'https://api.github.com'


def Git_Hub_API():
    results = requests.get(url)
    print("Type Results", type(results))
    print("Status Code: ", results.status_code)
    print("Headers: Content-Type: ", results.headers['Content-Type'])
    print("Headers: ", results.headers)

    etag = results.headers['ETag']
    print("ETag: ", etag)
    results1 = requests.get(url, headers={'If-None-Match': etag})
    print("Type Results", type(results1))
    print("Status Code: ", results1.status_code)
    print("Headers: Content-Type: ", results1.headers['Content-Type'])

    return results


if __name__ == '__main__':
    results = Git_Hub_API().json()
