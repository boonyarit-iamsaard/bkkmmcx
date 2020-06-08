from flask import Flask, render_template, request, redirect, url_for
import pymysql
import query

app = Flask(__name__)
conn = pymysql.connect("us-cdbr-east-05.cleardb.net", "b02b9837c2f815", "1628b5ed", "heroku_13912b51418014f")


# conn = pymysql.connect("localhost", "root", "cxbkkeng", "cxbkkeng")


@app.route("/")
def dashboard():
    def flight():
        with conn:
            cur = conn.cursor()
            cur.ping(reconnect=True)
            cur.execute(query.totalflt)
            total = cur.fetchall()
            return total

    flight = flight()

    def check():
        with conn:
            cur = conn.cursor()
            cur.ping(reconnect=True)
            cur.execute(query.totalChk)
            airline = cur.fetchall()
            return airline

    check = check()

    def ovn():
        with conn:
            cur = conn.cursor()
            cur.ping(reconnect=True)
            cur.execute(query.totalOvn)
            totalovn = cur.fetchall()
            return totalovn

    ovn = ovn()

    def wy():
        with conn:
            cur = conn.cursor()
            cur.ping(reconnect=True)
            cur.execute(query.wy)
            totalwy = cur.fetchall()
            return totalwy

    wy = wy()

    def addclrd():
        with conn:
            cur = conn.cursor()
            cur.ping(reconnect=True)
            cur.execute(query.addclrd)
            add = cur.fetchone()
            return add

    totaladdclrd = addclrd()

    def addworked():
        with conn:
            cur = conn.cursor()
            cur.ping(reconnect=True)
            cur.execute(query.addworked)
            totaladd = cur.fetchone()
            return totaladd

    totaladdworked = addworked()

    def pkg():
        with conn:
            cur = conn.cursor()
            cur.ping(reconnect=True)
            cur.execute(query.pkg)
            totalpkg = cur.fetchone()
            return totalpkg

    pkg = pkg()

    # flight = data.0
    # check = data.1
    # ovn = data.2
    # wy = data.3
    # pkgadd = data.4
    # addclrd = data.5
    # addworked = data.6
    # pkg = data.7
    data = (flight, check, ovn, wy, totaladdclrd, totaladdworked, pkg)
    return render_template("dashboard.html", title='Dashboard', data=data)


@app.route('/create')
def create():
    def staff():
        with conn:
            cur = conn.cursor()
            cur.ping(reconnect=True)
            cur.execute(query.staff)
            namelist = cur.fetchall()
            return namelist

    name = staff()

    def eic():
        with conn:
            cur = conn.cursor()
            cur.ping(reconnect=True)
            cur.execute(query.eic)
            recentlyadded = cur.fetchall()
            return recentlyadded

    eic = eic()

    data = (name, eic)

    return render_template('create.html', title='Add Flight', data=data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        # Flight details
        arrdate = request.form['arrdate']
        airline = request.form['airline']
        fltno = request.form['fltno']
        prefix = request.form['prefix']
        acreg = request.form['acreg']
        ata = request.form['ata']
        atd = request.form['atd']
        bay = request.form['bay']
        chk = request.form['chk']
        # Servicing
        watersvc = request.form['watersvc']
        wastesvc = request.form['wastersvc']
        afac = request.form['afac']
        gpu = request.form['gpu']
        asu = request.form['asu']
        acu = request.form['acu']
        brk = request.form['brk']
        cherry = request.form['cherry']
        platform = request.form['platform']
        # Work Package & ADDs
        pkg = request.form['pkg']
        padd = request.form['padd']
        sadd = request.form['sadd']
        add = request.form['add']
        zadd = request.form['zadd']
        cadd = request.form['cadd']
        madd = request.form['madd']
        worked = request.form['work']
        # Overnight
        ovnbay = request.form['ovnbay']
        tpc = request.form['tpc']
        waterdrain = request.form['waterdrain']
        wastedrain = request.form['wastedrain']
        fueldrain = request.form['fueldrain']
        stand = request.form['stand']
        acwsh = request.form['acwsh']
        # Handling By
        mech1 = request.form['mech1']
        mech2 = request.form['mech2']
        eng = request.form['eic']
        tda = request.form['tda']
        # Flight remark
        fltrmk = request.form['fltrmk']
        record = request.form['record']
        print(type(arrdate))
        with conn.cursor() as cursor:
            cursor.ping(reconnect=True)
            sql = query.insert
            cursor.execute(sql, (arrdate, airline, fltno, prefix, acreg, ata, atd, bay, chk,
                                 watersvc, wastesvc, afac, gpu, asu, acu, brk, cherry, platform, int(pkg), int(padd),
                                 int(sadd), int(add),
                                 int(zadd), int(cadd), int(madd), int(worked), ovnbay, tpc, waterdrain, wastedrain,
                                 fueldrain, stand, acwsh,
                                 mech1, mech2, eng, tda, fltrmk, record))
            conn.commit()
        return redirect(url_for('recently'))


@app.route('/recently')
def recently():
    with conn:
        cur = conn.cursor()
        cur.ping(reconnect=True)
        cur.execute(query.recently)
        recentlyadded = cur.fetchall()
        return render_template('recently.html', title='Recently Added', data=recentlyadded)


# if __name__ == "__main__":
#     app.run(debug=True)
