#!/usr/bin/env python3

import requests
import config 
import logging as log
log.basicConfig()

url="https://www.duckdns.org/update?domains={site}&token={token}&ip"

log.info("Updating duckdns site {site}.duckdns.org".format(site=config.site))
r = requests.get(url.format(site=config.site, token=config.token))

log.info("Response: {code} {text}".format(code=r.status_code, text=r.text))
