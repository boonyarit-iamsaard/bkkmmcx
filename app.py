from flask import Flask, render_template, url_for
import pymysql
import query

app = Flask(__name__)
conn = pymysql.connect("us-cdbr-east-05.cleardb.net", "b02b9837c2f815", "1628b5ed", "heroku_13912b51418014f")


@app.route("/")
def dashboard():
    def flight():
        with conn:
            cur = conn.cursor()
            cur.execute(query.flightSql)
            total = cur.fetchall()
            return total

    rows = flight()

    def check():
        with conn:
            cur = conn.cursor()
            cur.execute(query.totalChk)
            airline = cur.fetchall()
            return airline

    columns = check()

    def ovn():
        with conn:
            cur = conn.cursor()
            cur.execute(query.totalOvn)
            totalovn = cur.fetchall()
            return totalovn

    x = ovn()

    def wy():
        with conn:
            cur = conn.cursor()
            cur.execute(query.wy)
            wy = cur.fetchall()
            return wy

    wy = wy()

    test = (rows, columns, x, wy)
    return render_template("base.html", data=test)


if __name__ == "__main__":
    app.run(debug=True)
