import csv
from datetime import datetime
import time

def test(path):
    date = str(datetime.today().strftime('%Y%m%d'))
    securityID = ['4648', '4624', '4625', '4672', '4778', '4779', '5140']
    success = 0
    failure = 0
    with open(path + '\\Security.csv', 'r') as f:
        # with open('C:\\temp\\logs\\'+date+'\\Security20201007.csv', 'r') as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            if row[0] in securityID:
                if row[6] == 'FailureAudit':
                    failure += 1
                if row[6] == 'SuccessAudit':
                    success += 1
        return success, failure


def Success(path):
    Dates = []
    SucessCount = []
    FailureCount =[]
    securityID = ['4648', '4624', '4625', '4672', '4778', '4779', '5140']
    with open(path + '\\Security.csv', 'r') as f:

        next(f)
        reader = csv.reader(f)
        for row in reader:
            if row[0] in securityID:
                if row[6] == 'SuccessAudit':
                    strDate = row[11]
                    then = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S %p')
                    str = then.strftime('%m/%d/%Y')
                    if str not in Dates:
                        Dates.append(str)
                        FailureCount.append(0)
                        SucessCount.append(1)
                    else:
                        index = Dates.index(str)
                        SucessCount[index] += 1
                if row[6] == 'FailureAudit':
                    strDate = row[11]
                    then = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S %p')
                    str = then.strftime('%m/%d/%Y')
                    if str not in Dates:
                        Dates.append(str)
                        FailureCount.append(1)
                    else:
                        index = Dates.index(str)
                        FailureCount[index] += 1
        return Dates,SucessCount,FailureCount

#Success()
# def linux():
#
#     with open('C:\\Users\\User\\Desktop\\authLogs.csv', 'r') as f:
#
#         next(f)
#         reader = csv.reader(f, delimiter = "|")
#         for row in reader:
#            print(row[3])


