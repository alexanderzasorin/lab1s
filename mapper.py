__author__ = 'Artem'
import sys
da = {}
for line in sys.stdin:
    col_ip, col_uid, col_country, col_banner, col_pay = line.strip().split(',')
    da[col_country] = col_pay
for i in da:
    sys.stdout.write(i + ',' + da[i])

