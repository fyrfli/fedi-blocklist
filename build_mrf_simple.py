from requests import request
from json import loads

# grab the text list into a python list
text_list = open('./blocklist.txt','r').read().split()
url = "https://thebad.space/api/v1/search"
newlist = open('new_mrf_simple.json','w')

mrf_simple_top = """
{
  "group": ":pleroma",
  "key": ":mrf_simple",
  "value": [
    {
      "tuple": [
        ":media_removal",
        [
          {
            "tuple": [
              "mastodon.social",
              "CSAM"
            ]
          },
          {
            "tuple": [
              "mastodon.world",
              "CSAM"
            ]
          },
          {
            "tuple": [
              "mastodon.online",
              "CSAM"
            ]
          }
        ]
      ]
    },
    {
      "tuple": [
        ":followers_only",
        [
          {
            "tuple": [
              "mastodon.social",
              "cos too big to fail or something"
            ]
          },
          {
            "tuple": [
              "mastodon.online",
              "cos too big to fail or something"
            ]
          },
          {
            "tuple": [
              "mastodon.world",
              "cos too big to fail or something"
            ]
          },
          {
            "tuple": [
              "fosstodon.org",
              "moderation bullshit"
            ]
          }
        ]
      ]
    },
    {
      "tuple": [
        ":reject",
        [
"""

print(mrf_simple_top, file=newlist)

first = True
for site in text_list:
    payload = { "url": site }
    headers = {"Content-Type": "application/json"}
    bsinfo = request("POST", url, json=payload, headers=headers)
    if bsinfo.status_code == 200:
        my_reasons = ''
        for location in loads(bsinfo.text)['locations']:
            if location['description'].lower() == 'no description':
                my_reasons += ''
            else:
                my_reasons += location['description'].replace('\r\n',' ').replace('"','')
    if first:
        mrf_entry = "\t\t{ \"tuple\": [ \"" + site + "\", \"" + my_reasons + "\" ] }"
        first = False
    else:
        mrf_entry = "\t\t,{ \"tuple\": [ \"" + site + "\", \"" + my_reasons + "\" ] }"

    print(mrf_entry, file=newlist)

print("]]}]}", file=newlist)
newlist.close()
