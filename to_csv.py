import os
import json
import csv

i = 0

with open('blocklist.txt', 'r') as txt_blocklist:
    blocklist_data = txt_blocklist.read().split()
    with open('blocklist.csv', 'w') as csvfile:
        writeout = csv.writer(csvfile, dialect='excel', delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        while i < len(blocklist_data):
            writeout.writerow([blocklist_data[i],'Suspend'])
            i += 1
        
