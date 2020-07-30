# -*- conding: utf-8 -*-

import sys
import os
import subprocess
import configparser


from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.TagResourcesRequest import TagResourcesRequest

Filename = "./2.txt"
cmd = "sed -i '$d' "+Filename

def get_last_line(filename):
    
    try:
        filesize = os.path.getsize(filename)
        if filesize == 0:
            print (filename+" is null")
            return None
        else:
            with open(filename,'rb') as fp:
                offset = -2
                while -offset < filesize:
                    fp.seek(offset,2)
                    lines = fp.readlines()
                    if len(lines) >1:
                        data = lines[-1]
                        return data
                    else:
                        offset *=2
                fp.seek(0)
                lines = fp.readlines()
                data = lines[-1]
                return data
    except IOError:
        print(filename+'not found!')
def get_access():
    conf = configparser.ConfigParser()
    conf.read("./.config.ini", encoding="utf8")
    ak = conf.get('access','AK')
    sk = conf.get('access','SK')
    return ak,sk


def del_last_line():
    os.system( "sed -i '$d' ./2.txt >/dev/null")

def log_file(cmd_log):
    cmd_log=cmd_log
    subprocess.Popen(cmd_log, shell=True,)
    
def update_tag():
    try:

        line = get_last_line(Filename).split()
        if len(line) > 0:
            ResourceType = line[0].decode('utf-8')
            ResourceIds = line[1].decode('utf-8')
            Tag_Value = line[2].decode('utf-8')
            RegionId = line[3].decode('utf-8')
        else:
            print("----------------end---------------")
    except AttributeError:
        print("已经全部完成")
    try:
        ak,sk = get_access()
        client = AcsClient(ak, sk, RegionId)
        request = TagResourcesRequest()
        request.set_accept_format('json')
        request.set_ResourceType(ResourceType)
        request.set_ResourceIds([ResourceIds])
        request.set_Tags([
            {
                "Key": "CodeName-New",
                "Value": Tag_Value
            }
    
        ])
    except UnboundLocalError:
        print ("update end.")
        exit()
    try:
        response = client.do_action_with_exception(request)
        RequestId = str(response, encoding='utf-8')
        print(RequestId)
    except Exception as e:
        log = '"ResourceType:'+ResourceType+'  ResourceIds:'+ResourceIds+'  RegionId:'+RegionId+'  ResourceIds not use"'
        cmd_log = "echo "+ log + ">> update_tag.log"
        log_file(cmd_log)
        #print ("%s-->%s-->%s  update fail" %(ResourceType,ResourceIds,RegionId))
        del_last_line()
    try:
        if len(RequestId) == 52:
            log = '"ResourceType:'+ResourceType+'  ResourceIds:'+ResourceIds+'  RegionId:'+RegionId+'  update  success."'
            cmd_log = "echo "+ log +" >> update_tag.log"
            log_file(cmd_log)
            print ("%s-->%s-->%s  update success" %(ResourceType,ResourceIds,RegionId)) 
            del_last_line()
        else:
            log = '"ResourceType:'+ResourceType+'  ResourceIds:'+ResourceIds+'  RegionId:'+RegionId+'  update  fail"'
            cmd_log = "echo "+ log + ">> update_tag.log"
            log_file(cmd_log)
            print ("%s-->%s-->%s  update fail" %(ResourceType,ResourceIds,RegionId))
            del_last_line()
    except UnboundLocalError:
        print("ResourceIds 不存在,len() error")
def main():

    update_tag()
    while True:
        a = input("继续按n，退出请按其他:")
        if a == "n":
            update_tag()
        else:
            exit()
if __name__=='__main__':
    main()

