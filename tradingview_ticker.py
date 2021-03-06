""" Tradingview ticker """
import pymysql.cursors
from sa_func import get_broker_affiliate_link
from sa_db import sa_db_access
ACCESS_OBJ = sa_db_access()
DB_USR = ACCESS_OBJ.username()
DB_PWD = ACCESS_OBJ.password()
DB_NAME = ACCESS_OBJ.db_name()
DB_SRV = ACCESS_OBJ.db_server()

def get_tradingview_ticker(uid):
    """ Get tradingview ticker """
    return_data = ''
    ltvs = ''
    ide = 0
    referral_id = 'smartalpha'
    url = get_broker_affiliate_link('Tradingview', 'baseurl')
    theme = 'dark'
    connection = pymysql.connect(host=DB_SRV,
                                 user=DB_USR,
                                 password=DB_PWD,
                                 db=DB_NAME,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor(pymysql.cursors.SSCursor)

    sql = "SELECT id FROM users WHERE uid='"+ str(uid) +"'"
    cursor.execute(sql)
    res = cursor.fetchall()
    for row in res:
        ide = row[0]

    sql = "SELECT DISTINCT "+\
    "symbol_list.tradingview, symbol_list.symbol "+\
    "FROM instruments "+\
    "JOIN portfolios ON instruments.symbol = portfolios.portf_symbol "+\
    "JOIN symbol_list ON portfolios.symbol = symbol_list.symbol "+\
    "WHERE instruments.owner='"+ str(ide) +"' "
    cursor.execute(sql)
    res = cursor.fetchall()
    i = 1
    sep = ''
    for row in res:
        if i == 1:
            sep = ''
        else:
            sep = ','

        ltvs = ltvs + sep + '{"description": "'+ str(row[1]) +'", "proName": "'+ str(row[0]) +'"}'
        i += 1
    return_data = ' '+\
    '<div class="tradingview-widget-container">'+\
    ' <div class="tradingview-widget-container__widget"></div>'+\
    '  <div class="tradingview-widget-copyright">'+\
    '  <script type="text/javascript" '+\
    'src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>'+\
    '  {'+\
    '  "symbols": ['+\
    ltvs +\
    '  ],'+\
    '  "colorTheme": "'+ theme +'",'+\
    '  "isTransparent": true,'+\
    '  "largeChartUrl": "'+ url +'",'+\
    '  "displayMode": "adaptive",'+\
    '  "locale": "en",'+\
    '  "referral_id": "'+ referral_id +'"'+\
    '}'+\
    '  </script>'+\
    '</div>'+\
    '</div>'
    cursor.close()
    connection.close()
    return return_data
