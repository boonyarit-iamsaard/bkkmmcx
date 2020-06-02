from flask import Flask, render_template
import pymysql

app = Flask(__name__)
conn = pymysql.connect("localhost", "root", "cxbkkeng", "cxbkkstn")

flightSql = """SELECT airline, 
            COUNT(CASE WHEN MONTH(arrdate) = 1 THEN airline END) AS 'JAN',
            COUNT(CASE WHEN MONTH(arrdate) = 2 THEN airline END) AS 'FEB',
            COUNT(CASE WHEN MONTH(arrdate) = 3 THEN airline END) AS 'MAR',
            COUNT(CASE WHEN MONTH(arrdate) = 4 THEN airline END) AS 'APR',
            COUNT(CASE WHEN MONTH(arrdate) = 5 THEN airline END) AS 'MAY',
            COUNT(CASE WHEN MONTH(arrdate) = 6 THEN airline END) AS 'JUN',
            COUNT(CASE WHEN MONTH(arrdate) = 7 THEN airline END) AS 'JUL',
            COUNT(CASE WHEN MONTH(arrdate) = 8 THEN airline END) AS 'AUG',
            COUNT(CASE WHEN MONTH(arrdate) = 9 THEN airline END) AS 'SEP',
            COUNT(CASE WHEN MONTH(arrdate) = 10 THEN airline END) AS 'OCT',
            COUNT(CASE WHEN MONTH(arrdate) = 11 THEN airline END) AS 'NOV',
            COUNT(CASE WHEN MONTH(arrdate) = 12 THEN airline END) AS 'DEC'
            FROM fltlog 
            WHERE ata IS NOT NULL AND chk != 'RTB' 
            GROUP BY airline"""

totalChk = """SELECT airline, chk, 
            COUNT(CASE WHEN MONTH(arrdate) = 1 THEN chk END) AS 'JAN',
            COUNT(CASE WHEN MONTH(arrdate) = 2 THEN chk END) AS 'FEB',
            COUNT(CASE WHEN MONTH(arrdate) = 3 THEN chk END) AS 'MAR',
            COUNT(CASE WHEN MONTH(arrdate) = 4 THEN chk END) AS 'APR',
            COUNT(CASE WHEN MONTH(arrdate) = 5 THEN chk END) AS 'MAY',
            COUNT(CASE WHEN MONTH(arrdate) = 6 THEN chk END) AS 'JUN',
            COUNT(CASE WHEN MONTH(arrdate) = 7 THEN chk END) AS 'JUL',
            COUNT(CASE WHEN MONTH(arrdate) = 8 THEN chk END) AS 'AUG',
            COUNT(CASE WHEN MONTH(arrdate) = 9 THEN chk END) AS 'SEP',
            COUNT(CASE WHEN MONTH(arrdate) = 10 THEN chk END) AS 'OCT',
            COUNT(CASE WHEN MONTH(arrdate) = 11 THEN chk END) AS 'NOV',
            COUNT(CASE WHEN MONTH(arrdate) = 12 THEN chk END) AS 'DEC'
            FROM fltlog 
            WHERE chk != 'RTB' 
            GROUP BY airline, chk"""


@app.route("/")
def dashboard():
    def flight():
        with conn:
            cur = conn.cursor()
            cur.execute(flightSql)
            total = cur.fetchall()
            return total

    rows = flight()

    def check():
        with conn:
            cur = conn.cursor()
            cur.execute(totalChk)
            airline = cur.fetchall()
            return airline

    columns = check()
    test = (rows, columns)
    return render_template("base.html", data=test)


if __name__ == "__main__":
    app.run(debug=True)
