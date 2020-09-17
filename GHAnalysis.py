import json
import os
import sys
import getopt
def data_init(path_to_data):
    files=os.listdir(path_to_data)  #数据文件夹中json文件的文件名列表
    f=open('data_file.json','w',encoding='utf-8')
    for file in files:
        file_adr=path_to_data+"\\"+file      
        with open(file_adr,encoding='utf-8') as f1:
            for x in f1:
                f.write(x) #将所有json文件放入data_file.json中
    return 


def request_num(all_data,type_,actor_login,repo_name):
    num=0
    if repo_name=="-1":               #个人的 4 种事件的数量
        for data_comp in all_data:
            if actor_login==data_comp['actor']['login']:
                if type_==data_comp['type']:
                    num+=1
                else:
                    continue
            else:
                continue
    elif actor_login=="-1":           #每一个项目的 4 种事件的数量
        for data_comp in all_data:
            if repo_name==data_comp['repo']['name']:
                if type_==data_comp['type']:
                    num+=1
                else:
                    continue
            else:
                continue
    else:
        for data_comp in all_data:
            if repo_name==data_comp['repo']['name'] and actor_login==data_comp['actor']['login']:
                if type_==data_comp['type']:
                    num+=1
                else:
                    continue
            else:
                continue
    return num
if __name__ == "__main__":
    opts,arvs= getopt.getopt(sys.argv[1:],'i:u:r:e:',['user=','repo=','event=','init='])
    all_data1=[]
    type__="-1"
    actor_login_="-1"
    repo_name_="-1"
    path=""
    for opt in opts:
        if opt[0]=="-i" or opt[0]=="--init":
            path=opt[1]
            data_init(path)
            break
        elif opt[0]=="-u" or opt[0]=="--user":
            actor_login_=opt[1]
        elif opt[0]=="-r" or opt[0]=="--repo":
            repo_name_=opt[1]
        else:
             type__=opt[1]
    #data_init(path)
    da=open('data_file.json','r',encoding='utf-8')
    for x in da:
        y=json.loads(x)
        all_data1.append(y)
    number=request_num(all_data1,type__,actor_login_,repo_name_)
    print(number)
        
    
    
    
    
    
