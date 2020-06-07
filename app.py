from flask import Flask, render_template, url_for
import pymysql
import query

app = Flask(__name__)
# conn = pymysql.connect("us-cdbr-east-05.cleardb.net", "b02b9837c2f815", "1628b5ed", "heroku_13912b51418014f")


conn = pymysql.connect("localhost", "root", "cxbkkeng", "cxbkkstn")


@app.route("/")
def dashboard():
    def flight():
        with conn:
            cur = conn.cursor()
            cur.execute(query.flightSql)
            total = cur.fetchall()
            return total

    flight = flight()

    def check():
        with conn:
            cur = conn.cursor()
            cur.execute(query.totalChk)
            airline = cur.fetchall()
            return airline

    check = check()

    def ovn():
        with conn:
            cur = conn.cursor()
            cur.execute(query.totalOvn)
            totalovn = cur.fetchall()
            return totalovn

    ovn = ovn()

    def wy():
        with conn:
            cur = conn.cursor()
            cur.execute(query.wy)
            totalwy = cur.fetchall()
            return totalwy

    wy = wy()

    def pkgadd():
        with conn:
            cur = conn.cursor()
            cur.execute(query.pkdadd)
            totalpkgadd = cur.fetchall()
            return totalpkgadd

    pkgadd = pkgadd()

    def sumadd():
        with conn:
            cur = conn.cursor()
            cur.execute(query.sumadd)
            totaladd = cur.fetchone()
            return totaladd

    sumadd = sumadd()

    # flight = data.0
    # check = data.1
    # ovn = data.2
    # wy = data.3
    # pkgadd = data.4
    # sumadd = data.5
    datas = (flight, check, ovn, wy, pkgadd, sumadd)
    return render_template("dashboard.html", data=datas)


@app.route('/create')
def create():
    return render_template('create.html')


if __name__ == "__main__":
    app.run(debug=True)
