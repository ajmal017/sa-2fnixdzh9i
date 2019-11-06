
from app_cookie import *
from sa_db import *
from sa_func import *
access_obj = sa_db_access()
import pymysql.cursors
from print_google_ads import *
from tradingview_symbol_info import *


db_usr = access_obj.username(); db_pwd = access_obj.password(); db_name = access_obj.db_name(); db_srv = access_obj.db_server()

def get_details_header(uid,burl):
    connection = pymysql.connect(host=db_srv,user=db_usr,password=db_pwd, db=db_name,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    cr_s = connection.cursor(pymysql.cursors.SSCursor)
    sql_s = "SELECT symbol_list.symbol, feed.short_title, feed.content, feed.badge, feed.asset_class, feed.market, symbol_list.isin FROM symbol_list "+\
    "JOIN feed ON symbol_list.symbol = feed.symbol WHERE symbol_list.uid =" + str(uid) + " LIMIT 1"
    cr_s.execute(sql_s)
    rs_s = cr_s.fetchall()
    for row in rs_s:
        symbol = row[0]
        instr_name = row[1]
        content = row[2].replace('{burl}',burl)
        badge = row[3]
        asset_class = row[4]
        market = row[5]
        isin = row[6]

        if len(isin)>1:
            isin = ' | ISIN: '+ str(isin)
        else:
            isin = ''

    if (badge.find('-0') == -1 and badge.find('-1') == -1 and
    badge.find('-2') == -1 and badge.find('-3') == -1 and
    badge.find('-4') == -1 and badge.find('-5') == -1 and
    badge.find('-6') == -1 and badge.find('-7') == -1 and
    badge.find('-8') == -1 and badge.find('-9') == -1) :
        badge_class = 'badge badge-success'
    else:
        badge_class = 'badge badge-danger'
    badge_tooltip = 'Expected returns in the next 7 days'

    header_float_right = ''
    header_portfolio_info = ''
    if symbol.find(get_portf_suffix()) == -1:
        header_float_right = '<div style="margin: 0px; height: 100%; overflow: hidden;">' + get_tradingview_symbol_info(uid) + '</div>'
    else:
        header_float_right = print_google_ads('small_leaderboard','right')
        header_portfolio_info = ''+\
        '                <span class="title"><font style="font-size: x-large;">'+ instr_name +'&nbsp;<span class="'+badge_class+'" data-toggle="tooltip" data-placement="right" title="'+ badge_tooltip +'" >'+badge+'</span></font></span><br />'+\
        '                <span class="text"><span class="desc">'+ content + ' | ' + asset_class + market + symbol + isin +'</span></span>'

    p_header = '' +\
    '        <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">'+\
    '            <div class="box-part rounded" style="'+ theme_return_this('','border-style:solid; border-width:thin; border-color:#343a40;') +'">'+\
    header_float_right +\
    header_portfolio_info +\
    '            </div>'+\
    '        </div>'

    cr_s.close()
    connection.close()
    return p_header
