import cx_Oracle
import datetime
import re
import sys
import xlwt
import os

os.environ["NLS_LANG"] = ".AL32UTF8"
ip = '${SERVER_OP}'
port = 1521
service_name = '${DB_NAME}'
dsn = cx_Oracle.makedsn(ip, port, service_name)
connection = cx_Oracle.connect("${DB_USERNAME}", "${DB_PASSWORD}", dsn)
cursor = connection.cursor()

path = "/path/to/folder/"
FILENAME = path+"Sub-Dealer_" + str(datetime.datetime.now().date()) + ".csv"

#####your query headers goes here below is an example
STATEMENT = '''
SELECT DISTINCT a.USER_NAME,
                B.FIRST_NAME_V,
                B.LAST_NAME_V,
                B.DP_FIXED_IP,
                a.CREATION_DATE
  FROM tbl_user a
       LEFT OUTER JOIN TBL_USER_PERSONALINFO b ON A.CID = B.USER_ID_N
 WHERE A.TYPE = 'Dealer' AND A.SUB_TYPE = 'A'
'''

cursor.execute(STATEMENT)
result=cursor.fetchall()

##print result,"\n"

REPORT_STRING ="USER_NAME,FIRST_NAME_V,LAST_NAME_V,DP_FIXED_IP,CREATION_DATE"+"\n"
with open(FILENAME, 'a') as f:
    f.write(REPORT_STRING)
    f.close()

for each in result:
#    print "EACH: ",each,"\n"
    REPORT_STRING=""
    for ozv in each:
       REPORT_STRING += str(ozv) + ","



    with open(FILENAME, 'a') as f:
       f.write(REPORT_STRING + "\n")
       f.close()

##os.remove(FILENAME)
print "FINISHED"

####this will email the attach file
email="echo 'Please find attachement.' | mailx -s 'Sub Dealer Report' -A "+FILENAME+" mehdi.pourh@mtnirancell.ir"

#print(email)
os.system(email)

sys.exit
Ò
