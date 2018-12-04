#!/usr/bin/env python

import requests
import config
url="https://www.duckdns.org/update?domains={site}&token={token}&ip"

r = requests.get(url.format(site=config.site, token=config.token))

print(r.text)


