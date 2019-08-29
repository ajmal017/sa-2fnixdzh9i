# Copyright (c) 2018-present, Taatu Ltd.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from app_cookie import *
from sa_db import *
access_obj = sa_db_access()
import pymysql.cursors
from sa_func import *
from gcharts_columnchart import *

db_usr = access_obj.username(); db_pwd = access_obj.password(); db_name = access_obj.db_name(); db_srv = access_obj.db_server()


def get_signal_return_colchart(uid):
    r = ''
    chart_id = 'chart_signal_returns_col'
    title = ''
    legend_position = 'none'
    width = '100%'
    height = '100'
    color_neg = theme_return_this('red','red')
    color_pos = theme_return_this('green','lime')
    data = []
    data_label = []
    data_color = []
    data_annotation = []
    l_y1 = '1-year'
    l_m6 = '6-month'
    l_m3 = '3-month'
    l_m1 = '1-month'
    l_w1 = '1-week'

    try:
        connection = pymysql.connect(host=db_srv,user=db_usr,password=db_pwd, db=db_name,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        cr = connection.cursor(pymysql.cursors.SSCursor)
        sql = 'SELECT instruments.y1_signal,instruments.m6_signal,instruments.m3_signal,instruments.m1_signal,instruments.w1_signal, instruments.unit '+\
        'FROM instruments JOIN symbol_list ON symbol_list.symbol = instruments.symbol WHERE symbol_list.uid = '+ str(uid)
        cr.execute(sql)
        rs = cr.fetchall()

        for row in rs: y1 = row[0]; m6 = row[1]; m3 = row[2]; m1 = row[3]; w1 = row[4]; unit = row[5]

        data.append(y1)
        data_label.append(l_y1)
        if y1 < 0:
            data_color.append(color_neg)
        else:
            data_color.append(color_pos)
        if unit == '%':
            data_annotation.append( str(y1*100) + unit )
        else:
            data_annotation.append( str(y1) +' '+ unit )

        data.append(m6)
        data_label.append(l_m6)
        if m6 < 0:
            data_color.append(color_neg)
        else:
            data_color.append(color_pos)
        if unit == '%':
            data_annotation.append( str(m6*100) + unit )
        else:
            data_annotation.append( str(m6) +' '+ unit )

        data.append(m3)
        data_label.append(l_m3)
        if m3 < 0:
            data_color.append(color_neg)
        else:
            data_color.append(color_pos)
        if unit == '%':
            data_annotation.append( str(m3*100) + unit )
        else:
            data_annotation.append( str(m3) +' '+ unit )

        data.append(m1)
        data_label.append(l_m1)
        if m1 < 0:
            data_color.append(color_neg)
        else:
            data_color.append(color_pos)
        if unit == '%':
            data_annotation.append( str(m1*100) + unit )
        else:
            data_annotation.append( str(m1) +' '+ unit )

        data.append(w1)
        data_label.append(l_w1)
        if w1 < 0:
            data_color.append(color_neg)
        else:
            data_color.append(color_pos)
        if unit == '%':
            data_annotation.append( str(w1*100) + unit )
        else:
            data_annotation.append( str(w1) +' '+ unit )

        r = get_gcharts_column(chart_id,data,data_label,data_color,data_annotation,title,legend_position,width,height)
        cr.close()
        connection.close()

    except Exception as e: print(e)
    return r
