#定义界面函数
def info_print():
    print('请选择功能----------------')
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员')
    print('4.查询学员')
    print('5.显示所有学员')
    print('6.退出系统')
    print('-'*20)

info =[]
#添加功能函数
def add_info():
    new_id=input('请输入学号')
    new_name=input('请输入姓名')
    new_tel=input('请输入手机号')
    global info
    for i in info:
        if new_name== i['name']:
            print('此用户已经存在')#这里重点了解
            return #这里直接退出了大函数

    info_dict={}
    info_dict['id']=new_id
    info_dict['name']=new_name
    info_dict['tel']=new_tel
    info.append(info_dict)

def del_info():
    del_name=input('请输入你想删除的名字')
    global info
    for i in info:
        if del_name==i['name']:
            info.remove(i)
            break   #退出就近循环
        else:
            print('学员不存在')
        print('info')
def modify_info():
    modify_name=input('请输入名字')
    global info
    for i in info:
        if modify_name==i['name']:
            i['tel']=input('请输入修改的手机号')
            break
        else:
            print('该学员不存在')
    print(info)

def get_info():
    get_name=input('请输入名字')
    global info
    for i in info:
       if get_name==i['name']:
           print(f"该学员的学号是{i['id']},该学员的名字是{i['name']},该学员的手机号是{i['tel']}")
           break
       else:
           print('查无此人')
def print_all():
    for i in info:
        print(f'{i["id"]},{i["name"]},{i["tel"]}')
#系统输入6方才退出
while True:                                                   
 info_print()
#2.用户输入功能序号
 user_num=int(input('请输入功能序号'))
#如果用户输入
 if user_num==1:
    add_info()
 elif user_num==2:
    del_info()
 elif user_num==3:
    modify_info()
 elif user_num==4:
    get_info()
 elif user_num==5:
    print_all()
 elif user_num==6:
     exit_flag=input('yes?')
     if exit_flag=='yes':
         print('退出')
         break#作用是跳出最近的循环，可以是for 也可以是while！！！！
 else:
    print('输入有误')