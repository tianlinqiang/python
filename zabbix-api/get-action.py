# coding:utf8
import requests
import json
import configparser
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 定义url头部信息
headers = {'Content-Type': 'application/json-rpc'}  # zabbix地址
server_ip = '192.168.81.100'
# zabbix url
url = 'http://%s/zabbix/api_jsonrpc.php' % server_ip
host = 'https://cmdb.yeahmobi.com/api/v1'
data_dir = ''
def get_access(tokens):

    conf = configparser.ConfigParser()
    conf.read("access.ini", encoding="utf8")
    if tokens == "cmdb":
        username_cmdb = conf.get('access', 'username_cmdb')
        password_cmdb = conf.get('access', 'password_cmdb')
        return username_cmdb, password_cmdb
    elif tokens == "zabbix":
        username_zabbix = conf.get('zabbix', 'username_zabbix')
        password_zabbix = conf.get('zabbix', 'password_zabbix')
        return username_zabbix, password_zabbix



# 获取zabbix 的 token
def get_zabbix_Token():
    username, passwd = get_access("zabbix")
    data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": username,
            "password": passwd
        },
        "id": 0

    }

    request = requests.post(url=url, headers=headers, data=json.dumps(data))
    dict = json.loads(request.text)
    return dict['result']

def get_action():
    token = get_zabbix_Token()
    data = {
    "jsonrpc": "2.0",
    "method": "action.get",
    "params": {
        "output": "extend",
        "selectOperations": "extend",
        "selectRecoveryOperations": "extend",
        "selectFilter": "extend",
        "filter": {
            "eventsource": 2
        },
    },
    "auth": token,
    "id": 12
}

    request = requests.post(url=url, headers=headers, data=json.dumps(data))
    dict = json.loads(request.content)
    all_servers_json = json.dumps(dict, sort_keys=False, indent=4, separators=(',', ': '))
    f = open(data_dir + 'get_action_json.json', 'w')
    f.write(all_servers_json)
    print dict

get_action()


