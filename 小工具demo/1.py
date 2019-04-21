import requests

url = 'https://www.bilibili.com/video/av44593630'
download_url = "http://upos-hz-mirrorks3u.acgvideo.com/upgcxcode/52/36/78063652/78063652-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEVEuxTEto8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&deadline=1552235396&gen=playurl&nbs=1&oi=2053122100&os=ks3u&platform=pc&trid=f79daaafd74a4f6b8b02132468c73d3a&uipk=5&upsig=d8a41a567ef9c702cc31535ac8588a59"

my_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Accept': 'application/json, text/plain, */*'
}

download_headers = {
    'Origin': 'https://www.bilibili.com',
    'Referer': 'https://www.bilibili.com/video/av45841853',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Accept': 'application/json, text/plain, */*'
}

# res = requests.get(url=url, headers=my_headers, verify=False)
res = requests.get(url=download_url, headers=download_headers, verify=False)

# print(res.text)

with open('hi2.mp4', 'wb') as f:
    f.write(res.content)
