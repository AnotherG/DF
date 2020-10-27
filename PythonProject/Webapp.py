from werkzeug.exceptions import HTTPException
from flask import Flask, render_template, request, redirect, url_for, session
import Flitering as FL
import LinuxFunctions as Linux1
import WindowFunctions as WF

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Start Scripting':
            # CR.create_logs()
            path = request.form['text']
            session['path'] = path
            # How to use find()
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
    a, b = FL.test(path)
    date,app,sys,sec = WF.countEntries(path)
    return render_template('main.html', suc=a, fai=b,dates=date,apps=app,syss=sys,secs=sec)


@app.route('/Security', methods=['GET', 'POST'])
def Security():
    path = session['path']
    a, b = FL.test(path)
    Dates, Count, Failure = FL.Success(path)
    if request.method == 'POST':
        if request.form.get("submit_a"):
            pass
        # Dates, Count= FL.Success()
        elif request.form.get("submit_b"):
            print("helloaqwer")

    return render_template('Security.html', suc=a, fai=b, data=Count, labels=Dates, failure=Failure)

@app.route('/Application', methods=['GET', 'POST'])
def Application():
    path = session['path']
    cat, dump = WF.Application(path, "Error")
    if request.method == 'POST':
        type1 = request.form["buttonName"]
        dump= WF.appDump(path, type1)
        return render_template('Application.html', cats=cat, dumps=dump, chosen=type1)

    return render_template('Application.html',cats=cat,dumps=dump,chosen="Error")


@app.route('/System', methods=['GET', 'POST'])
def System():
    path = session['path']
    cat, installation, dump, lame1 = WF.AppEntryType(path, "Error")
    if request.method == 'POST':
        type1 = request.form["buttonName"]
        dump = WF.dumpFunction(path, type1)
        return render_template('System.html', cats=cat, installations=installation, dumps=dump, lame1s=lame1,chosen=type1)

    return render_template('System.html', cats=cat, installations=installation, dumps=dump, lame1s=lame1, chosen="Error")

@app.route('/raw', methods=['GET', 'POST'])
def raw():
    path = session['path']
    type1="Application"
    dump = WF.raw(path,type1)
    if request.method == 'POST':
        if request.form.get("Application"):
            print("1")
            type1="Application"
        if request.form.get("System"):
            print("2")
            type1="System"
        if request.form.get("Security"):
            print("3")
            type1="Security"
        dump = WF.raw(path, type1)
        return render_template('raw.html', dumps=dump)
    return render_template('raw.html',dumps=dump)


# ----------------------------------------------WINDOW END--------------------------------------------------------#
#ERROR HANDLING (Remove errors)
# @app.errorhandler(Exception)
# def handle_exception(e):
#     return render_template("404.html", e=e)


if __name__ == '__main__':
    #app.register_error_handler(404,handle_exception)
    app.run(debug=True)
