# Copyright (c) 2018-present, Taatu Ltd.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from sa_db import *
access_obj = sa_db_access()
import pymysql.cursors


db_usr = access_obj.username(); db_pwd = access_obj.password(); db_name = access_obj.db_name(); db_srv = access_obj.db_server()

def get_aggregate_perf():

    box_content = ''

    try:
        '''
        connection = pymysql.connect(host=db_srv,user=db_usr,password=db_pwd, db=db_name,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        cr = connection.cursor(pymysql.cursors.SSCursor)
        sql = "SELECT "
        cr.execute(sql)
        rs = cr.fetchall()
        for row in rs:
            symbol = row[0]
        '''

        l_title_aggregate_perf = 'Your Performance'

        box_content = '' +\
        '            <div class="box-part rounded" style="height: 465px;">'+\
        '               <span class="sectiont"><i class="fas fa-chart-area"></i>&nbsp;'+ l_title_aggregate_perf +'</span>'+\
        '            </div>'

        '''
        cr.close()
        connection.close()
        '''

    except Exception as e: print(e)

    return box_content

def get_control_center(burl):

    box_content = ''

    try:
        '''
        connection = pymysql.connect(host=db_srv,user=db_usr,password=db_pwd, db=db_name,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        cr = connection.cursor(pymysql.cursors.SSCursor)
        sql = "SELECT "
        cr.execute(sql)
        rs = cr.fetchall()
        for row in rs:
            symbol = row[0]
        '''

        l_title_control_center = 'Control Center'

        box_content = '' +\
        '            <div class="box-part rounded" style="height: 250px;">'+\
        '               <span class="sectiont"><i class="fas fa-tasks"></i>&nbsp;'+ l_title_control_center +'</span>'+\
        '            </div>'

        '''
        cr.close()
        connection.close()
        '''

    except Exception as e: print(e)

    return box_content


def get_control_center_aggregate_perf(burl):
    r = ''
    try:
        r = '<div class="col-lg-6 col-md-12 col-sm-12 col-xs-12">'+\
        get_control_center(burl)+\
        get_aggregate_perf()+\
        '</div>'

    except Exception as e: print(e)
    return r