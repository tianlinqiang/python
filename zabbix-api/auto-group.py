# -*- coding: utf-8 -*-
import requests
import json
import configparser
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 定义url头部信息
headers = {'Content-Type': 'application/json-rpc'}  # zabbix地址
server_ip = '10.1xxxxxxx:8888'
url = 'http://%s/zabbix/api_jsonrpc.php' % server_ip
host = 'https://xxxxxxxxxxxxxxxxx/api/v1'

# data_dir = '/etc/zabbix/python_script/data_json/'
# path_access = '/etc/zabbix/python_script/'
path_access = ""
data_dir = ""

class get_token:
    def __init__(self, token):
        self.token = token
    def get_access(self):
        conf = configparser.ConfigParser()
        conf.read( path_access + "access.ini", encoding="utf8")
        if self.token == "cmdb":
            username = conf.get('access', 'username_cmdb')
            password = conf.get('access', 'password_cmdb')
            return username, password
        elif self.token == "zabbix":
            username = conf.get('zabbix', 'username_zabbix')
            password = conf.get('zabbix', 'password_zabbix')
            return username, password
    def get_zabbix_Token(self):
        username, passwd = self.get_access()
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

    def get_cmdb_token(self):
        username, passwd = self.get_access()
        auth_token = None
        url = '{}/auth'.format(host)
        # print(url)
        query_args = {
            "username": username,
            "password": passwd,
            "type": "normal"
        }
        try:
            response = requests.post(url, data=query_args)
            auth_token = json.loads(response.text)['auth_token']
        except:
            pass
        return auth_token


class zabbix_data:
    def need_update_hostgroup(self):
        all_data = {}
        token = get_token("zabbix").get_zabbix_Token()
        data = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": ["hostid", "name", "status"],
                "selectGroups": ["groupid", "name"],
            },
            "auth": token,
            "id": 1
        }
        request = requests.post(url=url, headers=headers, data=json.dumps(data))
        dict = json.loads(request.content)
        for x in range(len(dict['result'])):
            a_list = []
            hostid = dict['result'][x]["hostid"]
            hostname = dict['result'][x]["name"]
            status = dict['result'][x]["status"]
            if str(dict['result'][x]["status"]) == "0":
                for j in range(len(dict['result'][x]["groups"])):
                    b = {}
                    b[dict['result'][x]["groups"][j]["groupid"]] = dict['result'][x]["groups"][j]["name"]
                    a_list.append(b)
                all_data[hostid + "#" + hostname+"#"+status] = a_list
        a_dict = {}
        for key in all_data.keys():
            for i in all_data[key]:
                if str(i.values()[0]).startswith("Project"):
                    a_dict[key] = all_data[key]
        b_dict = list(set(all_data.keys()) - set(a_dict.keys()))
        c_dict = {}
        for i in b_dict:
            c_list = []
            for j in all_data.keys():
                if i == j:
                    c_dict[i] = all_data[j]
                    c_list.append(c_dict)
        w_dict = {}
        for key in c_dict.keys():
            w_list = []
            for j in c_dict[key]:
                w_list.append(j.keys()[0])
            w_dict[key] = w_list
        return w_dict

class get_codename_pro_dept_id:
    def get_codename(self):  # 获取所有的codename列表

        token = get_token("cmdb").get_cmdb_token()
        params = {
            'page_size': 1000,
            'page': 1
        }

        url = "{}/application/get_codename".format(host)
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer %s" % token
        }
        response = requests.get(url, params=params, headers=headers)
        res = json.loads(response.text)
        return res

    def codename_load_json_dict(self):  ##读本地保存的项目-部门-codename关系的json文件
        load_json = open(data_dir + 'Project_Department_Codename.json', 'r')
        Project_Department_Codename = json.load(load_json)
        return Project_Department_Codename

    def getGroupid(self):
        token = get_token("zabbix").get_zabbix_Token()
        group = {}
        data = {"jsonrpc": "2.0",
                "method": "hostgroup.get",
                "params": {
                    "output": ["groupid", "name"]
                },
                "auth": token,
                "id": 0
                }

        request = requests.post(url=url, headers=headers, data=json.dumps(data))
        dict = json.loads(request.content)
        for i in dict['result']:
            groupid = i['groupid']
            name = i['name']
            group[name] = groupid
        return group

    def get_action_data(self,codename):
        code_list = self.get_codename()
        data = self.codename_load_json_dict()['results']
        group_id = self.getGroupid()
        action_data = []

        for i in code_list:
            a = {}
            if "CodeName_" + i in group_id.keys():
                id = group_id["CodeName_" + i]
                a["ID_codename"] = id
                a["codename"] = i
            for j in range(len(data)):
                if i == data[j]["codename"]:
                    project = data[j]['project_extra_info']['name']
                    department = data[j]['department_extra_info']['name']
                    id_pro = group_id["Project_" + project]
                    id_dept = group_id["Department_" + department]
                    a["ID_project"] = id_pro
                    a["ID_deparment"] = id_dept
                    action_data.append(a)
        need_add_groups = []
        for i in action_data:
            if i.get("codename") == codename:
                need_add_groups.append(i.get("ID_codename"))
                need_add_groups.append(i.get("ID_deparment"))
                need_add_groups.append(i.get("ID_project"))
        return need_add_groups


class get_hostname_codename:
    def all_server_info(self):  ##读本地保存的项目-部门-codename关系的json文件
        load_json = open(data_dir + 'all_server_list.json', 'r')
        all_server = json.load(load_json)
        return all_server

    def get_codename(self,hostIP):
        b = []
        all_server = self.all_server_info()["results"]
        for i in all_server:
                if hostIP in str(i.get("private_ip")):
                    return i.get("codename")

class get_zabbix_hostid_hostip:

    def get_zabbix_hostid(self,zabbix_hostid):
        token = get_token("zabbix").get_zabbix_Token()
        a_list = []
        data = {"jsonrpc": "2.0",
                "method": "hostinterface.get",
                "params": {
                    "output": ["hostid", "ip", "name"]
                },
                "auth": token,
                "id": 0
                }

        request = requests.post(url=url, headers=headers, data=json.dumps(data))
        dict = json.loads(request.content)
        for i in dict['result']:
            a_dict = {}
            hostid = i['hostid']
            hostip = i['ip']
            a_dict["hostid"] = hostid
            a_dict["hostip"] = hostip
            a_list.append(a_dict)
        for i in a_list:
            if i.get("hostid") == zabbix_hostid:
                return i.get("hostip")

class zabbix_update_groups:
    def get_zabbix_update_host_group(self,update_data):
        token = get_token("zabbix").get_zabbix_Token()
        if update_data:
            i = update_data.keys()[0]
            data = {
                "jsonrpc": "2.0",
                "method": "host.update",
                "params": {
                    "hostid": i,
                    "groups": update_data[i]
                },
                "auth": token,
                "id": 10
            }
            request = requests.post(url=url, headers=headers, data=json.dumps(data))
            dict = json.loads(request.content)
            print dict
        else:
            exit()


def main():

    zabbix_datas  = zabbix_data()
    need_update_hostgroups = zabbix_datas.need_update_hostgroup()
    print need_update_hostgroups
    print len(need_update_hostgroups)
    hostID_hostIP = get_zabbix_hostid_hostip()
    codenames = get_hostname_codename()
    new_groups = get_codename_pro_dept_id()
    do_updata_group = zabbix_update_groups()
    for i in need_update_hostgroups.keys():
        update_data = {}
        hostID = str(i).split("#")[0]
        hostname = str(i).split("#")[1]
        hostIP = hostID_hostIP.get_zabbix_hostid(hostID)
        codename = codenames.get_codename(hostIP)
        new_need_add_groups = new_groups.get_action_data(codename)
        old_groups = need_update_hostgroups[i]
        if new_need_add_groups:
            #print hostID, hostname, codename, old_groups, new_need_add_groups
            new_update_data = old_groups+new_need_add_groups
            new_update_data = list(set(new_update_data))
            a_list = []
            for j in new_update_data:
                a_dict = {}
                a_dict["groupid"]=j
                a_list.append(a_dict)
            update_data[hostID] = a_list
            print update_data
            do_updata_group.get_zabbix_update_host_group(update_data)
        else:
            print 'no update.'
            exit()
if __name__ == '__main__':
    main()
