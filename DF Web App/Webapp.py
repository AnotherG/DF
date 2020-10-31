from werkzeug.exceptions import HTTPException
from flask import Flask, render_template, request, redirect, url_for, session
import LinuxFunctions as Linux1
import WindowFunctions as WF

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# ----------------------------------------------START PAGE---------------------------------------------------------#
@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Go':
            path = request.form['text']
            session['path'] = path
            if (path.find('linux') != -1):
                return redirect('/LinuxOverview')
            else:
                return redirect('/LoginLogs')

    return render_template('startPage.html')


# ----------------------------------------------LINUX START---------------------------------------------------------#
@app.route('/LinuxOverview', methods=['GET', 'POST'])
def LinuxOverview():
    path = session['path']
    lastlog = Linux1.LastLogs(path)
    usb = Linux1.USB(path)
    su = Linux1.su(path)
    message = Linux1.syslogs(path)
    return render_template('linuxOverview.html', lastlogs=lastlog, usbs=usb, sus=su, messages=message)


@app.route('/LinuxUsers', methods=['GET', 'POST'])
def LinuxUsers():
    path = session['path']
    user = Linux1.ReadUsers(path)
    last = Linux1.Last(path, "root")
    command = Linux1.readCommands(path, "root")
    lastb = Linux1.LoginFailure(path, "root")
    if request.method == 'POST':
        name = request.form["text"]
        last = Linux1.Last(path, name)
        command = Linux1.readCommands(path, name)
        lastb = Linux1.LoginFailure(path, name)
    return render_template('linuxUsers.html', users=user, lasts=last, lastbs=lastb, commands=command)


# ----------------------------------------------LINUX END--------------------------------------------------------#

# ----------------------------------------------WINDOW START--------------------------------------------------------#
@app.route('/LoginLogs')
def LoginLogs():
    path = session['path']
    date, app, sys, sec = WF.countEntries(path)
    return render_template('main.html', dates=date, apps=app, syss=sys, secs=sec)


@app.route('/Security', methods=['GET', 'POST'])
def Security():
    path = session['path']
    Dates, Count = WF.SecurityLogsData(path)
    criticalEvent, serviceEvent, loginEvent, userAccEvent, comAccEvent, sgEvent, objEvent, crptoEvent, networkEvent, \
    ipEvent, hashEvent = WF.SecurityTable(path, 'NULL')
    if request.method == 'POST':
        dateinfo = request.form["buttonName"]
        criticalEvent, serviceEvent, loginEvent, userAccEvent, comAccEvent, sgEvent, objEvent, crptoEvent, networkEvent, \
        ipEvent, hashEvent = WF.SecurityTable(path, dateinfo)

    return render_template('Security.html', data=Count, labels=Dates, serviceEvent=serviceEvent,
                           loginEvent=loginEvent, criticalEvent=criticalEvent, userAccEvent=userAccEvent,
                           comAccEvent=comAccEvent, sgEvent=sgEvent, objEvent=objEvent, crptoEvent=crptoEvent,
                           networkEvent=networkEvent, ipEvent=ipEvent, hashEvent=hashEvent)


@app.route('/Application', methods=['GET', 'POST'])
def Application():
    path = session['path']
    cat, dump = WF.Application(path, "Error")
    if request.method == 'POST':
        type1 = request.form["buttonName"]
        dump = WF.appDump(path, type1)
        return render_template('Application.html', cats=cat, dumps=dump, chosen=type1)

    return render_template('Application.html', cats=cat, dumps=dump, chosen="Error")


@app.route('/System', methods=['GET', 'POST'])
def System():
    path = session['path']
    cat, installation, dump, lame1 = WF.AppEntryType(path, "Error")
    if request.method == 'POST':
        type1 = request.form["buttonName"]
        dump = WF.dumpFunction(path, type1)
        return render_template('System.html', cats=cat, installations=installation, dumps=dump, lame1s=lame1,
                               chosen=type1)

    return render_template('System.html', cats=cat, installations=installation, dumps=dump, lame1s=lame1,
                           chosen="Error")


@app.route('/raw', methods=['GET', 'POST'])
def raw():
    path = session['path']
    type1 = "Application"
    dump = WF.raw(path, type1)
    if request.method == 'POST':
        if request.form.get("Application"):
            type1 = "Application"
        if request.form.get("System"):
            type1 = "System"
        if request.form.get("Security"):
            type1 = "Security"
        dump = WF.raw(path, type1)
        return render_template('raw.html', dumps=dump)
    return render_template('raw.html', dumps=dump)


@app.route('/Timeline', methods=['GET', 'POST'])
def Timeline():
    path = session['path']
    prefetch, Pcount, Pdate, Pcreation, Pwritten = WF.prefetch(path)
    recents, Rcount, Rdate, Rcreation, Rwritten = WF.recent(path)
    lsm = WF.LSM(path)
    wlan = WF.wlan(path)
    return render_template('timeline.html', prefetch=prefetch, recent=recents, lsm=lsm, wlan=wlan, Pcounts=Pcount,
                           Pdates=Pdate
                           , Pcreation=Pcreation, Pwritten=Pwritten, Rcounts=Rcount, Rdates=Rdate, Rcreation=Rcreation,
                           Rwritten=Rwritten)


# ----------------------------------------------WINDOW END--------------------------------------------------------#
# ----------------------------------------------ERROR HANDLING START----------------------------------------------#
#@app.errorhandler(Exception)
#def handle_exception(e):
#    return render_template("404.html", e=e)
# ----------------------------------------------ERROR HANDLING END------------------------------------------------#

if __name__ == '__main__':
    #app.register_error_handler(404, handle_exception)
    app.run(debug=True)
