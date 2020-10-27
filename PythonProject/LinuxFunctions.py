import csv

def ReadUsers(path):
    items = []
    with open(path + '\\userList.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            an_item = dict(user=row[0])
            items.append(an_item)
    return items


def Last(path, user):
    items = []
    with open(path + '\\last\\' + user + '.txt', 'r') as f:
        reader = csv.reader(f, delimiter="|")
        for row in reader:
            if row[0] == user:
                an_item = dict(user=row[0], sh=row[1], loc=row[2], time=row[3])
                items.append(an_item)
        return items


def LoginFailure(path, user):
    items = []
    with open(path + '\\lastb\\' + user + '.txt', 'r') as f:
        reader = csv.reader(f, delimiter="|")
        for row in reader:
            if row[0] == user:
                an_item = dict(user=row[0], sh=row[1], loc=row[2], time=row[3])
                items.append(an_item)
        return items


def readCommands(path, user):
    items = []
    with open(path + '\\history\\' + user + '.txt', 'r') as f:
        reader = csv.reader(x.replace('\0', '') for x in f)

        for row in reader:
            if not row:
                next(f)
            else:
                an_item = dict(command=row[0])
                items.append(an_item)
        return items


def LastLogs(path):
    items = []
    with open(path + '\\lastLog.csv', 'r') as f:
        reader = csv.reader(f, delimiter="|")
        next(f)
        for row in reader:
            an_item = dict(user=row[0], port=row[1], from1=row[2], latest=row[3])
            items.append(an_item)
        return items


def USB(path):
    items = []
    with open(path + '\\kernLogs.csv', 'r') as f:
        reader = csv.reader(f, delimiter="|")
        next(f)
        i = 0
        for row in reader:
            if row[3].find("New USB device found") == -1:
                i += 1
                pass
            else:
                next(reader)[3]
                b = (next(reader)[3])
                a = (next(reader)[3])
                c = (next(reader)[3])
                if c.find("SerialNumber") == -1:
                    an_item = dict(time=row[0],man=a.split(':')[-1], product=b.split(':')[-1], sn="None")
                else:
                    an_item = dict(time=row[0],man=a.split(':')[-1], product=b.split(':')[-1], sn=c.split(':',2)[-1])
                items.append(an_item)
        return items

def su(path):
    items = []
    with open(path + '\\authLogs.csv', 'r') as f:
        reader = csv.reader(x.replace('\0', '') for x in f)

        next(f)
        for row in reader:
            if row[0].find("su:") == -1:
                pass
            else:
                if row[0].find("to ") == -1:
                    pass
                else:
                    an_item = dict(time=row[0].split("|")[0], su=row[0].split("|")[-2])
                    items.append(an_item)
        return items

def syslogs(path):
    items = []
    with open(path + '\\syslogs.csv', 'r',encoding="utf8") as f:
        reader = csv.reader(f, delimiter="|")
        next(f)
        for row in reader:
            if row[3].find("warning") == -1:
                if row[3].find("error") == -1:
                    pass
                    if row[3].find("critical") == -1:
                        pass
                    else:
                        an_item = dict(time=row[0], services=row[2], message=row[3], level ="Critical")
                        items.append(an_item)
                else:
                    an_item = dict(time=row[0], services=row[2], message=row[3], level ="Error")
                    items.append(an_item)
            else:
                an_item = dict(time=row[0], services=row[2], message=row[3], level ="Warning")
                items.append(an_item)
        return items
syslogs("C:\\Users\\User\\Desktop\\qwer\\temp\\logs\\linux\\20201025")