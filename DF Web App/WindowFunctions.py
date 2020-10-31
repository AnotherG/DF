import csv

# -----------------------------------SYSTEM START-----------------------------------#
from datetime import datetime


def AppEntryType(path, type):
    items = []
    installationItems = []
    dumpLIST = []
    lame1 = []
    with open(path + '\\System.csv', 'r') as f:
        reader = csv.reader(f)
        next(f)
        next(f)
        information = 0
        warning = 0
        critical = 0
        error = 0
        for row in reader:
            if row[0] == "1":
                if row[7].find("Possible detection of CVE") == -1:
                    pass
                else:
                    message = row[7].split("\n")[0]
                    message = message.split(":", 1)[1]
                    stranger_danger = dict(name=row[13], date=row[11], message=message)
                    lame1.append(stranger_danger)
            if row[0] == "7045":
                name = row[7].split("\n")[2]
                name = name.split(":", 1)[1]

                filepath = row[7].split("\n")[3]
                filepath = filepath.split(":", 1)[1]

                time = row[11]
                user = row[13]

                an_item = dict(name=name, filepath=filepath, time=time, user=user)
                installationItems.append(an_item)
            # ----------dump messages-----------------#
            if row[6] == type:
                dump = dict(time=row[11], user=row[13], message=row[7])
                dumpLIST.append(dump)
            # ----------category type-----------------#
            if row[6] == "Information":
                information += 1
            elif row[6] == "Warning":
                warning += 1
            elif row[6] == "Critical":
                critical += 1
            elif row[6] == "Error":
                error += 1

        items.append(warning)
        items.append(information)
        items.append(error)
        items.append(critical)

    return items, installationItems, dumpLIST, lame1


def dumpFunction(path, type):
    items = []
    with open(path + '\\System.csv', 'r') as f:
        reader = csv.reader(f)
        next(f)
        next(f)
        for row in reader:
            if row[6] == type:
                dump = dict(time=row[11], user=row[13], message=row[7])
                items.append(dump)
        return items


# -----------------------------------SYSTEM END-----------------------------------#
# -----------------------------------APPLICATION START-----------------------------------#
def Application(path, type):
    items = []
    dumpLIST = []
    with open(path + '\\Application.csv', 'r') as f:
        reader = csv.reader(f)
        next(f)
        next(f)
        information = 0
        warning = 0
        critical = 0
        error = 0
        for row in reader:
            # ----------dump messages-----------------#
            if row[6] == type:
                dump = dict(time=row[11], user=row[8], message=row[7])
                dumpLIST.append(dump)
            # ----------category type-----------------#
            if row[6] == "Information":
                information += 1
            elif row[6] == "Warning":
                warning += 1
            elif row[6] == "Critical":
                critical += 1
            elif row[6] == "Error":
                error += 1

        items.append(warning)
        items.append(information)
        items.append(error)
        items.append(critical)
        # ----------category type-----------------#
    return items, dumpLIST


def appDump(path, type):
    items = []
    with open(path + '\\Application.csv', 'r') as f:
        reader = csv.reader(f)
        next(f)
        next(f)
        for row in reader:
            if row[6] == type:
                dump = dict(time=row[11], user=row[8], message=row[7])
                items.append(dump)
        return items


# -----------------------------------APPLICATION END-----------------------------------#
# -----------------------------------STARTPAGE START-----------------------------------#
def countEntries(path):
    Dates = []
    appC = []
    sysC = []
    secC = []
    with open(path + '\\Application.csv', 'r') as f:
        reader = csv.reader(f)
        next(f)
        next(f)
        for row in reader:
            current = row[11].split(" ")[0]
            if current not in Dates:
                Dates.append(current)
                appC.append(0)
                sysC.append(0)
                secC.append(0)
            if current in Dates:
                index = Dates.index(current)
                appC[index] += 1
    with open(path + '\\System.csv', 'r') as f:
        reader = csv.reader(f)
        next(f)
        next(f)
        for row in reader:
            current = row[11].split(" ")[0]
            if current in Dates:
                index = Dates.index(current)
                sysC[index] += 1
                appC[index] += 1
    with open(path + '\\Security.csv', 'r') as f:
        reader = csv.reader(f)
        next(f)
        next(f)
        for row in reader:
            current = row[11].split(" ")[0]
            if current in Dates:
                index = Dates.index(current)
                secC[index] += 1
    Dates.reverse()
    appC.reverse()
    sysC.reverse()
    secC.reverse()
    return Dates, appC, sysC, secC

# -----------------------------------STARTPAGE END-----------------------------------#
# -----------------------------------RAW START-----------------------------------#
def raw(path, type):
    items = []
    if type == "Application":

        with open(path + '\\Application.csv', 'r') as f:
            reader = csv.reader(f)
            next(f)
            next(f)
            for row in reader:
                dump = dict(EventID=row[0], MachineName=row[1], Data=row[2], Index=row[3], Category=row[4],
                            CategoryNumber=row[5],
                            EntryType=row[6], Message=row[7], Source=row[8], ReplacementStrings=row[9],
                            InstanceId=row[10], TimeGenerated=row[11], TimeWritten=row[12], UserName=row[13])
                items.append(dump)

    if type == "System":
        with open(path + '\\System.csv', 'r') as f:
            reader = csv.reader(f)
            next(f)
            next(f)
            for row in reader:
                dump = dict(EventID=row[0], MachineName=row[1], Data=row[2], Index=row[3], Category=row[4],
                            CategoryNumber=row[5],
                            EntryType=row[6], Message=row[7], Source=row[8], ReplacementStrings=row[9],
                            InstanceId=row[10], TimeGenerated=row[11], TimeWritten=row[12], UserName=row[13])
                items.append(dump)
    if type == "Security":
        with open(path + '\\Security.csv', 'r') as f:
            reader = csv.reader(f)
            next(f)
            next(f)
            for row in reader:
                dump = dict(EventID=row[0], MachineName=row[1], Data=row[2], Index=row[3], Category=row[4],
                            CategoryNumber=row[5],
                            EntryType=row[6], Message=row[7], Source=row[8], ReplacementStrings=row[9],
                            InstanceId=row[10], TimeGenerated=row[11], TimeWritten=row[12], UserName=row[13])
                items.append(dump)
    return items


# -----------------------------------RAW END-----------------------------------#
# -----------------------------------Timeline START-----------------------------------#
def prefetch(path):
    items = []
    Dates = []
    accessC = []
    creationC = []
    writtenC = []
    with open(path + '\\Prefetch.csv', 'r') as f:
        reader = csv.reader(f)
        next(f)
        next(f)
        for row in reader:
            an_item = dict(file=row[11], creation=row[19], access=row[21], write=row[23])
            items.append(an_item)

            accessDate = row[21].split(" ")[0]
            creationDate = row[19].split(" ")[0]
            writtenDate = row[23].split(" ")[0]
            if accessDate not in Dates:
                Dates.append(accessDate)
                accessC.append(0)
                creationC.append(0)
                writtenC.append(0)
            if accessDate in Dates:
                index = Dates.index(accessDate)
                accessC[index] += 1
            if creationDate in Dates:
                index = Dates.index(creationDate)
                creationC[index] += 1
            if writtenDate in Dates:
                index = Dates.index(writtenDate)
                writtenC[index] += 1

        Dates.reverse()
        accessC.reverse()
        creationC.reverse()
        writtenC.reverse()
        return items, accessC, Dates, creationC, writtenC


def recent(path):
    items = []
    Dates = []
    accessC = []
    creationC = []
    writtenC = []
    with open(path + '\\Recent.csv', 'r') as f:
        reader = csv.reader(f)
        next(f)
        next(f)
        for row in reader:
            an_item = dict(file=row[10], creation=row[16], access=row[18], write=row[20])
            items.append(an_item)

            accessDate = row[18].split(" ")[0]
            creationDate = row[16].split(" ")[0]
            writtenDate = row[20].split(" ")[0]
            if accessDate not in Dates:
                Dates.append(accessDate)
                accessC.append(0)
                creationC.append(0)
                writtenC.append(0)
            if accessDate in Dates:
                index = Dates.index(accessDate)
                accessC[index] += 1
            if creationDate in Dates:
                index = Dates.index(creationDate)
                creationC[index] += 1
            if writtenDate in Dates:
                index = Dates.index(writtenDate)
                writtenC[index] += 1

        Dates.reverse()
        accessC.reverse()
        creationC.reverse()
        writtenC.reverse()
        return items, accessC, Dates, creationC, writtenC


def LSM(path):
    item = []
    with open(path + '\\TerminalServices-LocalSessionManager.csv', 'r') as f:
        reader = csv.reader(f)
        next(f)
        next(f)
        for row in reader:
            if row[1] == "21" or row[1] == "23":

                message = row[0].split("\n")[0]
                message = message.split(":")[1]
                user = row[0].split("\n")[2]
                user = user.split(": ")[1]
                sessionid = row[0].split("\n")[3]
                sessionid = sessionid.split(":")[1]
                time = row[16]
                if row[1] == "21":
                    source = row[0].split("\n")[4]
                    source = source.split(": ")[1]
                    an_item = dict(time=time, message=message, user=user, sessionid=sessionid, source=source)
                else:
                    an_item = dict(time=time, message=message, user=user, sessionid=sessionid, source="")
                item.append(an_item)

        return item


def wlan(path):
    item = []
    with open(path + '\\WLAN-AutoConfig.csv', 'r') as f:
        reader = csv.reader(f)
        next(f)
        next(f)
        for row in reader:
            if row[1] == "11005" or row[1] == "11004":
                message = row[0].split("\n")[0].split(".")[0]
                ssid = row[0].split("\n")[5].split(": ")[1]
                time = row[16]
                an_item = dict(time=time, message=message, ssid=ssid, modes="")
                item.append(an_item)
            if row[1] == "11010":
                message = row[0].split("\n")[0].split(".")[0]
                ssid = row[0].split("\n")[5].split(": ")[1]
                time = row[16]
                modes = row[0].split("\n", 7)[-1]
                an_item = dict(time=time, message=message, ssid=ssid, modes=modes)
                item.append(an_item)
        return item


# -----------------------------------Timeline END-----------------------------------#
# -----------------------------------SECURITY START-----------------------------------#

def SecurityLogsData(path):
    AllDateCount = []
    Date_Count = {}
    securityID = ['4648', '4624', '4625', '4672', '4649', '4670', '4695', '4697', '4720',
                  '4722',
                  '4723', '4724', '4725', '4626', '4738', '4740', '4767', '4780', '4781', '4794', '5376', '5377',
                  '4741',
                  '4742', '4743', '4727', '4728', '4729', '4730', '4731', '4732', '4733', '4734', '4735', '4737',
                  '4754',
                  '4755', '4756', '4757', '4758', '4764', '4656', '4658', '4660', '4663', '5038', '5041', '5042',
                  '5043',
                  '5044', '5045', '5046', '5047', '5048', '5049', '5065', '5067', '5143', '5144']

    with open(path + '\\Security.csv', 'r') as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            if row[0] in securityID:
                strDate = row[11]
                then = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S %p')
                str = then.strftime('%d/%m/%Y')
                if str not in Date_Count:
                    Date_Count[str] = 1
                else:
                    Date_Count[str] += 1

        DateList = list(Date_Count.keys())
        DateCount = list(Date_Count.values())
        DateCount.reverse()
        DateList.reverse()
        return DateList, DateCount


def SecurityTable(path, date):
    Date = date
    if date == 'NULL':
        with open(path + '\\Security.csv', 'r') as a:
            reader = csv.reader(a)
            row1 = next(reader)
            row2 = next(reader)
            row3 = next(reader)
            strDate = row3[11]
            then = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S %p')
            Date = then.strftime('%d/%m/%Y')
            a.close()

    Critical = ['4649', '4695']
    Service = ['4697', ]
    Login = ['4625', '4624', '4648', '4672']
    # Login = ['4648']
    UserAccountManagement = ['4720', '4722', '4723', '4724', '4725', '4626', '4738', '4740', '4767', '4780', '4781',
                             '4794', '5376', '5377']
    ComputerAccountManagement = ['4741', '4742', '4743', ]
    SecurityGroupManagement = ['4727', '4728', '4729', '4730', '4731', '4732', '4733', '4734', '4735', '4737', '4754',
                               '4755',
                               '4756', '4757', '4758', '4764', ]
    Object = ['4656', '4658', '4660', '4663', '4670']
    CryptographicContext = ['5065', '5067']
    NetworkShare = ['5143', '5144']
    IPSec = ['5041', '5042', '5043', '5044', '5045', '5046', '5047', '5048', '5049']
    HashNotValid = ['5038']

    CriticalTable = []
    ServiceTable = []
    LoginTable = []
    UserAccountManagementTable = []
    ComputerAccountManagementTable = []
    SecurityGroupManagementTable = []
    ObjectTable = []
    CryptographicContextTable = []
    NetworkShareTable = []
    IPSecTable = []
    HashNotValidTable = []

    with open(path + '\\Security.csv', 'r') as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            if row[0] in Critical:
                strDate = row[11]
                then = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S %p')
                str = then.strftime('%d/%m/%Y')
                if str == Date:
                    dump = dict(id=row[0], machine=row[1], msg=row[7], source=row[8], time=row[11])
                    CriticalTable.append(dump)

            elif row[0] in Service:
                strDate = row[11]
                then = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S %p')
                str = then.strftime('%d/%m/%Y')
                if str == Date:
                    dump = dict(id=row[0], machine=row[1], msg=row[7], source=row[8], time=row[11])
                    ServiceTable.append(dump)

            elif row[0] in Login:
                strDate = row[11]
                then = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S %p')
                str = then.strftime('%d/%m/%Y')
                if str == Date:
                    dump = dict(id=row[0], machine=row[1], msg=row[7], source=row[8], time=row[11])
                    LoginTable.append(dump)

            elif row[0] in UserAccountManagement:
                strDate = row[11]
                then = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S %p')
                str = then.strftime('%d/%m/%Y')
                if str == Date:
                    dump = dict(id=row[0], machine=row[1], msg=row[7], source=row[8], time=row[11])
                    UserAccountManagementTable.append(dump)

            elif row[0] in ComputerAccountManagement:
                strDate = row[11]
                then = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S %p')
                str = then.strftime('%d/%m/%Y')
                if str == Date:
                    dump = dict(id=row[0], machine=row[1], msg=row[7], source=row[8], time=row[11])
                    ComputerAccountManagementTable.append(dump)

            elif row[0] in SecurityGroupManagement:
                strDate = row[11]
                then = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S %p')
                str = then.strftime('%d/%m/%Y')
                if str == Date:
                    dump = dict(id=row[0], machine=row[1], msg=row[7], source=row[8], time=row[11])
                    SecurityGroupManagementTable.append(dump)

            elif row[0] in Object:
                strDate = row[11]
                then = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S %p')
                str = then.strftime('%d/%m/%Y')
                if str == Date:
                    dump = dict(id=row[0], machine=row[1], msg=row[7], source=row[8], time=row[11])
                    ObjectTable.append(dump)

            elif row[0] in CryptographicContext:
                strDate = row[11]
                then = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S %p')
                str = then.strftime('%d/%m/%Y')
                if str == Date:
                    dump = dict(id=row[0], machine=row[1], msg=row[7], source=row[8], time=row[11])
                    CryptographicContextTable.append(dump)

            elif row[0] in NetworkShare:
                strDate = row[11]
                then = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S %p')
                str = then.strftime('%d/%m/%Y')
                if str == Date:
                    dump = dict(id=row[0], machine=row[1], msg=row[7], source=row[8], time=row[11])
                    NetworkShareTable.append(dump)

            elif row[0] in IPSec:
                strDate = row[11]
                then = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S %p')
                str = then.strftime('%d/%m/%Y')
                if str == Date:
                    dump = dict(id=row[0], machine=row[1], msg=row[7], source=row[8], time=row[11])
                    IPSecTable.append(dump)

            elif row[0] in HashNotValid:
                strDate = row[11]
                then = datetime.strptime(strDate, '%d/%m/%Y %H:%M:%S %p')
                str = then.strftime('%d/%m/%Y')
                if str == Date:
                    dump = dict(id=row[0], machine=row[1], msg=row[7], source=row[8], time=row[11])
                    HashNotValidTable.append(dump)

    return CriticalTable, ServiceTable, LoginTable, UserAccountManagementTable, ComputerAccountManagementTable, \
           SecurityGroupManagementTable, ObjectTable, \
           CryptographicContextTable, NetworkShareTable, IPSecTable, HashNotValidTable
# -----------------------------------Timeline END-----------------------------------#
