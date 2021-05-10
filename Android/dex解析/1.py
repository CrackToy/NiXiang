import requests

cookies = {
    'ts_refer': 'www.tencentwm.com/mb/v5/life/discussion/authorize.shtml',
    'qluin': '085e9858e1129ed877d5dfab6@wx.tenpay.com',
    'qlskey': 'v0957f29122606ffb540027cff52a8cb',
    'lct_qlskey': 'v0957f29122606ffb540027cff52a8cb',
    'qlappid': 'wxc92ca6e258e3f1eb',
    'is_forbidden': '0',
    'ts_last': '/mb/v5/life/discussion/index.shtml',
    'ts_uid': '171959642',
    'ts_sid': '4578323120',
}

headers = {
    'Host': 'www.txfund.com',
    'accept': 'application/json, text/plain, */*',
    'origin': 'https://www.txfund.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1320.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)',
    'content-type': 'application/x-www-form-urlencoded',
    'referer': 'https://www.txfund.com/mb/v5/life/discussion/index.shtml?stock_id=lct_m_1000000074&lctfrom=share',
    'accept-language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
}

params = (
    ('cmdname', 'get_topic_list'),
    ('_', '94517674'),
)

data = 'cmdname=get_topic_list&param=%7B%22stock_id%22%3A%22lct_m_1000000074%22%2C%22begin%22%3A%22%22%2C%22begin_score%22%3A%22%22%2C%22limit%22%3A10%2C%22order%22%3A%22comment%22%7D&hideLoading=true&g_tk=1489310485'

response = requests.post('https://www.txfund.com/lct_go/lct_comm_call_go.fcgi', headers=headers, params=params, cookies=cookies, data=data)
print(response.text)