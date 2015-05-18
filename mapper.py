__author__ = 'Artem'
import sys
for line in sys.stdin:
    col_ip, col_uid, col_country, col_banner, col_pay = line.strip().split(',')
    print (col_country + ',' + col_pay)

