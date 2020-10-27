import csv


# -----------------------------------SYSTEM START-----------------------------------#
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
        # ----------category type-----------------#
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
        print(items)
        return items


# -----------------------------------APPLICATION END-----------------------------------#

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
