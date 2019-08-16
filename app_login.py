# Copyright (c) 2018-present, Taatu Ltd.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from app_head import *; from app_body import *; from app_page import *
from sa_db import *
from sa_func import *
access_obj = sa_db_access()
import pymysql.cursors
from app_cookie import *

db_usr = access_obj.username(); db_pwd = access_obj.password(); db_name = access_obj.db_name(); db_srv = access_obj.db_server()

def user_logout(burl):

    resp = ''
    try:
        resp = make_response( redirect("/") )
        resp.set_cookie('user', '0')
    except Exception as e: print(e)

    return resp

def user_login(usr,pwd,burl,redirect):

    c = ''
    redirectUrl = burl + '?dashboard=1'

    try:
        connection = pymysql.connect(host=db_srv,user=db_usr,password=db_pwd, db=db_name,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        cr = connection.cursor(pymysql.cursors.SSCursor)
        usr = usr.lower()
        sql = "SELECT uid FROM users WHERE username ='"+ str(usr) +"' AND password ='"+ str(pwd) +"' LIMIT 1"
        print(sql)
        cr.execute(sql)
        rs = cr.fetchall()
        uid = ''
        for row in rs: uid = row[0]
        cr.close()
        connection.close()

        if redirect != '':
            redirectUrl = redirect

        if not uid == '':
            c = set_sa_cookie(uid, set_page( get_head('<meta http-equiv="refresh" content="0;URL=' + redirectUrl + '" />') + get_body('','') ) )
        else:
            c = set_page( get_head('<meta http-equiv="refresh" content="0;URL=' + burl + 'signin/?err=1" />') + get_body('','') )

    except Exception as e: print(e)

    return c
