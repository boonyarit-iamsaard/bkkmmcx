from flask import Flask, render_template, url_for
import pymysql
import query

app = Flask(__name__)
# conn = pymysql.connect("us-cdbr-east-05.cleardb.net", "b02b9837c2f815", "1628b5ed", "heroku_13912b51418014f")
conn = pymysql.connect("localhost", "root", "", "cxbkkeng")


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
            wy = cur.fetchall()
            return wy

    wy = wy()

    test = (flight, check, ovn, wy)
    return render_template("dashboard.html", data=test)


@app.route('/create')
def create():
    return render_template('create.html')


if __name__ == "__main__":
    app.run(debug=True)
