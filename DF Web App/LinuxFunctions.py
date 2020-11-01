import csv
import os


# Get list of users
def ReadUsers(path):
    items = []
    if os.stat(path + '\\userList.txt').st_size == 0:
        return items
    else:
        with open(path + '\\userList.txt', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                an_item = dict(user=row[0])
                items.append(an_item)
        return items


# last command
def Last(path, user):
    items = []
    if os.stat(path + '\\last\\' + user + '.txt').st_size == 0:
        return items
    else:
        with open(path + '\\last\\' + user + '.txt', 'r') as f:
            reader = csv.reader(f, delimiter="|")
            for row in reader:
                if row[0] == user:
                    an_item = dict(user=row[0], sh=row[1], loc=row[2], time=row[3])
                    items.append(an_item)
            return items


# last b command
def LoginFailure(path, user):
    items = []
    if os.stat(path + '\\lastb\\' + user + '.txt').st_size == 0:
        return items
    else:
        with open(path + '\\lastb\\' + user + '.txt', 'r') as f:
            reader = csv.reader(f, delimiter="|")
            for row in reader:
                if row[0] == user:
                    an_item = dict(user=row[0], sh=row[1], loc=row[2], time=row[3])
                    items.append(an_item)
            return items


# history command
def readCommands(path, user):
    items = []
    if os.stat(path + '\\history\\' + user + '.txt').st_size == 0:
        return items
    else:
        with open(path + '\\history\\' + user + '.txt', 'r') as f:
            reader = csv.reader(x.replace('\0', '') for x in f)

            for row in reader:
                print(row)
                if not row:
                    pass
                else:
                    an_item = dict(command=row[0])
                    items.append(an_item)
            return items


# lastlog command
def LastLogs(path):
    items = []
    if os.stat(path + '\\lastLog.csv').st_size == 0:
        return items
    else:
        with open(path + '\\lastLog.csv', 'r') as f:
            reader = csv.reader(f, delimiter="|")
            next(f)
            for row in reader:
                an_item = dict(user=row[0], port=row[1], from1=row[2], latest=row[3])
                items.append(an_item)
            return items




# getting list of newly installed usb devices from kern logs
def USB(path):
    items = []
    if os.stat(path + '\\kernLogs.csv').st_size == 0:
        return items
    else:
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
                        an_item = dict(time=row[0], man=a.split(':')[-1], product=b.split(':')[-1], sn="None")
                    else:
                        an_item = dict(time=row[0], man=a.split(':')[-1], product=b.split(':')[-1], sn=c.split(':', 2)[-1])
                    items.append(an_item)
            return items


# getting list of users who tried to su from auth logs
def su(path):
    items = []
    if os.stat(path + '\\authLogs.csv').st_size == 0:
        return items
    else:
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


# getting (warning, error, critical) messages from syslogs
def syslogs(path):
    items = []
    if os.stat(path + '\\syslogs.csv').st_size == 0:
        return items
    else:
        with open(path + '\\syslogs.csv', 'r', encoding="utf8") as f:
            reader = csv.reader(f, delimiter="|")
            next(f)
            for row in reader:
                if row[3].find("warning") == -1:
                    if row[3].find("error") == -1:
                        pass
                        if row[3].find("critical") == -1:
                            pass
                        else:
                            an_item = dict(time=row[0], services=row[2], message=row[3], level="Critical")
                            items.append(an_item)
                    else:
                        an_item = dict(time=row[0], services=row[2], message=row[3], level="Error")
                        items.append(an_item)
                else:
                    an_item = dict(time=row[0], services=row[2], message=row[3], level="Warning")
                    items.append(an_item)
            return items
