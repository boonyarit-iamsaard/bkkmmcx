from flask import Flask, render_template, request, redirect, url_for
import pymysql
import query

app = Flask(__name__)
conn = pymysql.connect("us-cdbr-east-05.cleardb.net", "b02b9837c2f815", "1628b5ed", "heroku_13912b51418014f")


# conn = pymysql.connect("localhost", "root", "22@Nov1985", "backup-bkkmmcx")


# test push to develop branch again

@app.route("/")
def dashboard():
    def flight():
        with conn:
            conn.ping(reconnect=True)
            cur = conn.cursor()
            cur.execute(query.total_flt)
            total = cur.fetchall()
            return total

    flight = flight()

    def check():
        with conn:
            conn.ping(reconnect=True)
            cur = conn.cursor()
            cur.execute(query.report_chk)
            airline = cur.fetchall()
            return airline

    check = check()

    def ovn():
        with conn:
            conn.ping(reconnect=True)
            cur = conn.cursor()
            cur.execute(query.total_ovn)
            totalovn = cur.fetchall()
            return totalovn

    ovn = ovn()

    def wy():
        with conn:
            conn.ping(reconnect=True)
            cur = conn.cursor()
            cur.execute(query.wy)
            totalwy = cur.fetchall()
            return totalwy

    wy = wy()

    def addclrd():
        with conn:
            conn.ping(reconnect=True)
            cur = conn.cursor()
            cur.execute(query.add_clrd)
            add = cur.fetchone()
            return add

    totaladdclrd = addclrd()

    def addworked():
        with conn:
            conn.ping(reconnect=True)
            cur = conn.cursor()
            cur.execute(query.add_worked)
            totaladd = cur.fetchone()
            return totaladd

    totaladdworked = addworked()

    def pkg():
        with conn:
            conn.ping(reconnect=True)
            cur = conn.cursor()
            cur.execute(query.pkg)
            totalpkg = cur.fetchone()
            return totalpkg

    pkg = pkg()

    # flight = data.0
    # check = data.1
    # ovn = data.2
    # wy = data.3
    # pkgadd = data.4
    # add_clrd = data.5
    # add_worked = data.6
    # pkg = data.7
    data = (flight, check, ovn, wy, totaladdclrd, totaladdworked, pkg)
    return render_template("dashboard.html", title='Dashboard', data=data)


@app.route('/create')
def create():
    def staff():
        with conn:
            conn.ping(reconnect=True)
            cur = conn.cursor()
            cur.execute(query.staff)
            namelist = cur.fetchall()
            return namelist

    name = staff()

    def eic():
        with conn:
            conn.ping(reconnect=True)
            cur = conn.cursor()
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
        with conn:
            conn.ping(reconnect=True)
            cur = conn.cursor()
            cur.execute(query.last)
            last = cur.fetchone()
            last = last[0] + 1
            sql = query.insert
            cur.execute(sql, (last, arrdate, airline, fltno, prefix, acreg, ata, atd, bay, chk,
                              watersvc, wastesvc, afac, gpu, asu, acu, brk, cherry, platform, int(pkg), int(padd),
                              int(sadd), int(add),
                              int(zadd), int(cadd), int(madd), int(worked), ovnbay, tpc, waterdrain, wastedrain,
                              fueldrain, stand, acwsh,
                              mech1, mech2, eng, tda, fltrmk, record))
            conn.commit()
        return redirect(url_for('flight_log'))


@app.route('/details/<string:id_data>', methods=['GET'])
def details(id_data):
    with conn:
        conn.ping(reconnect=True)
        cur = conn.cursor()
        cur.execute('SELECT * FROM flight WHERE fltid=%s', id_data)
        update_flight = cur.fetchone()
        cur.execute(query.staff)
        namelist = cur.fetchall()
        cur.execute(query.eic)
        eic = cur.fetchall()
        data = (update_flight, namelist, eic)
        return render_template('update.html', title='Update', data=data)


@app.route('/update/<string:id_data>', methods=['POST'])
def update(id_data):
    if request.method == 'POST':
        fltid = id_data
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
        with conn:
            conn.ping(reconnect=True)
            cur = conn.cursor()
            sql = query.update
            cur.execute(sql, (arrdate, airline, fltno, prefix, acreg, ata, atd, bay, chk,
                              watersvc, wastesvc, afac, gpu, asu, acu, brk, cherry, platform, int(pkg), int(padd),
                              int(sadd), int(add),
                              int(zadd), int(cadd), int(madd), int(worked), ovnbay, tpc, waterdrain, wastedrain,
                              fueldrain, stand, acwsh,
                              mech1, mech2, eng, tda, fltrmk, record, fltid))
            conn.commit()
        return redirect(url_for('flight_log'))


@app.route('/flight_log')
def flight_log():
    with conn:
        conn.ping(reconnect=True)
        cur = conn.cursor()
        cur.execute(query.flight_log)
        data = cur.fetchall()
        return render_template('flight_log.html', title='Flight Log', data=data)


@app.route('/report_chk')
def report_chk():
    with conn:
        conn.ping(reconnect=True)
        cur = conn.cursor()
        cur.execute(query.report_chk)
        chk = cur.fetchall()
        cur.execute('SELECT DISTINCT airline FROM flight ORDER BY airline')
        airline = cur.fetchall()
        data = (chk, airline)
        return render_template('report_chk.html', title='Reports-Check', data=data)


@app.route('/report_flt')
def report_flt():
    with conn:
        conn.ping(reconnect=True)
        cur = conn.cursor()
        cur.execute(query.total_flt)
        flt = cur.fetchall()
        cur.execute(query.total_ovn)
        ovn = cur.fetchall()
        data = (flt, ovn)
        return render_template('report_flt.html', title='Reports-Flight', data=data)


@app.route('/report_svc')
def report_svc():
    with conn:
        conn.ping(reconnect=True)
        cur = conn.cursor()
        cur.execute(query.count_h2osvc)
        count = cur.fetchall()
        cur.execute(query.detail_h2osvc)
        detail = cur.fetchall()
        cur.execute(query.count_wastesvc)
        count2 = cur.fetchall()
        cur.execute(query.detail_wastesvc)
        detail2 = cur.fetchall()
        data = (count, detail, count2, detail2)
        return render_template('report_svc.html', title='Reports-Servicing', data=data)


if __name__ == "__main__":
    app.run(debug=True)
