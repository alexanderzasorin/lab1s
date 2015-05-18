__author__ = 'Artem'
import sys
#c = open("mapper_input.txt", "r")
#for line in c:
for line in sys.stdin:
    col_ip, col_uid, col_country, col_banner, col_pay = line.strip().split(',')
    print (col_country + ',' + col_pay)

