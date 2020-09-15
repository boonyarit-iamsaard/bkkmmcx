total_flt = """SELECT COALESCE(airline, 'TOTAL'),
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
            COUNT(CASE WHEN MONTH(arrdate) = 12 THEN airline END) AS 'DEC',
            COUNT(airline) AS 'TOTAL'
            FROM flight
            WHERE ata IS NOT NULL AND chk != 'RTB'
            GROUP BY airline
            WITH ROLLUP"""

report_chk = """SELECT airline, chk, 
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
            FROM flight 
            GROUP BY airline, chk"""

total_ovn = """SELECT COALESCE(airline, 'TOTAL'), 
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
            COUNT(CASE WHEN MONTH(arrdate) = 12 THEN chk END) AS 'DEC',
            COUNT(airline) AS 'TOTAL'
            FROM flight 
            WHERE ata IS NOT NULL AND atd IS NULL AND chk != 'RTB' 
            GROUP BY airline
            WITH ROLLUP"""

add = """SELECT DATE_FORMAT(arrdate, '%M'), 
    SUM(padd) AS "PADD", 
    SUM(sadd) AS "SADD", 
    SUM('add') AS "ADD", 
    SUM(zadd) AS "ZADD", 
    SUM(cadd) AS "CADD", 
    SUM(madd) AS "MADD", 
    FROM fltlog"""

wy = """SELECT COALESCE(airline, 'TOTAL'), 
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
        COUNT(CASE WHEN MONTH(arrdate) = 12 THEN chk END) AS 'DEC',
        COUNT(chk) AS 'TOTAL'
        FROM flight 
        WHERE chk = 'WY' 
        GROUP BY airline
        WITH ROLLUP"""

add_clrd = """SELECT SUM(CASE WHEN MONTH(arrdate) = 1 THEN padd+sadd+nadd+zadd+cadd+madd ELSE 0 END) AS '1',
    SUM(CASE WHEN MONTH(arrdate) = 2 THEN padd+sadd+nadd+zadd+cadd+madd ELSE 0 END) AS '2',
    SUM(CASE WHEN MONTH(arrdate) = 3 THEN padd+sadd+nadd+zadd+cadd+madd ELSE 0 END) AS '3',
    SUM(CASE WHEN MONTH(arrdate) = 4 THEN padd+sadd+nadd+zadd+cadd+madd ELSE 0 END) AS '4',
    SUM(CASE WHEN MONTH(arrdate) = 5 THEN padd+sadd+nadd+zadd+cadd+madd ELSE 0 END) AS '5',
    SUM(CASE WHEN MONTH(arrdate) = 6 THEN padd+sadd+nadd+zadd+cadd+madd ELSE 0 END) AS '6',
    SUM(CASE WHEN MONTH(arrdate) = 7 THEN padd+sadd+nadd+zadd+cadd+madd ELSE 0 END) AS '7',
    SUM(CASE WHEN MONTH(arrdate) = 8 THEN padd+sadd+nadd+zadd+cadd+madd ELSE 0 END) AS '8',
    SUM(CASE WHEN MONTH(arrdate) = 9 THEN padd+sadd+nadd+zadd+cadd+madd ELSE 0 END) AS '9',
    SUM(CASE WHEN MONTH(arrdate) = 10 THEN padd+sadd+nadd+zadd+cadd+madd ELSE 0 END) AS '10',
    SUM(CASE WHEN MONTH(arrdate) = 11 THEN padd+sadd+nadd+zadd+cadd+madd ELSE 0 END) AS '11',
    SUM(CASE WHEN MONTH(arrdate) = 12 THEN padd+sadd+nadd+zadd+cadd+madd ELSE 0 END) AS '12'
    FROM flight"""

add_worked = """SELECT SUM(CASE WHEN MONTH(arrdate) = 1 THEN worked ELSE 0 END) AS '1',
    SUM(CASE WHEN MONTH(arrdate) = 2 THEN worked ELSE 0 END) AS '2',
    SUM(CASE WHEN MONTH(arrdate) = 3 THEN worked ELSE 0 END) AS '3',
    SUM(CASE WHEN MONTH(arrdate) = 4 THEN worked ELSE 0 END) AS '4',
    SUM(CASE WHEN MONTH(arrdate) = 5 THEN worked ELSE 0 END) AS '5',
    SUM(CASE WHEN MONTH(arrdate) = 6 THEN worked ELSE 0 END) AS '6',
    SUM(CASE WHEN MONTH(arrdate) = 7 THEN worked ELSE 0 END) AS '7',
    SUM(CASE WHEN MONTH(arrdate) = 8 THEN worked ELSE 0 END) AS '8',
    SUM(CASE WHEN MONTH(arrdate) = 9 THEN worked ELSE 0 END) AS '9',
    SUM(CASE WHEN MONTH(arrdate) = 10 THEN worked ELSE 0 END) AS '10',
    SUM(CASE WHEN MONTH(arrdate) = 11 THEN worked ELSE 0 END) AS '11',
    SUM(CASE WHEN MONTH(arrdate) = 12 THEN worked ELSE 0 END) AS '12'
    FROM flight"""

pkg = """SELECT SUM(CASE WHEN MONTH(arrdate) = 1 THEN pkg ELSE 0 END) AS '1',
    SUM(CASE WHEN MONTH(arrdate) = 2 THEN pkg ELSE 0 END) AS '2',
    SUM(CASE WHEN MONTH(arrdate) = 3 THEN pkg ELSE 0 END) AS '3',
    SUM(CASE WHEN MONTH(arrdate) = 4 THEN pkg ELSE 0 END) AS '4',
    SUM(CASE WHEN MONTH(arrdate) = 5 THEN pkg ELSE 0 END) AS '5',
    SUM(CASE WHEN MONTH(arrdate) = 6 THEN pkg ELSE 0 END) AS '6',
    SUM(CASE WHEN MONTH(arrdate) = 7 THEN pkg ELSE 0 END) AS '7',
    SUM(CASE WHEN MONTH(arrdate) = 8 THEN pkg ELSE 0 END) AS '8',
    SUM(CASE WHEN MONTH(arrdate) = 9 THEN pkg ELSE 0 END) AS '9',
    SUM(CASE WHEN MONTH(arrdate) = 10 THEN pkg ELSE 0 END) AS '10',
    SUM(CASE WHEN MONTH(arrdate) = 11 THEN pkg ELSE 0 END) AS '11',
    SUM(CASE WHEN MONTH(arrdate) = 12 THEN pkg ELSE 0 END) AS '12'
    FROM flight"""

staff = "SELECT name FROM staff"

eic = "SELECT name FROM staff WHERE role = 'LAME'"

insert = """INSERT INTO flight (fltid, arrdate, airline, fltno, prefix, acreg, ata, atd, bay, chk, 
    watersvc, wastesvc, afac, gpu, asu, acu, brk, cherry, platform, pkg, padd, sadd, nadd, 
    zadd, cadd, madd, worked, ovnbay, tpc, waterdrain, wastedrain, fueldrain, stand, wash, 
    mech1, mech2, eng, tda, fltrmk, record) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

update = """UPDATE flight SET arrdate=%s, airline=%s, fltno=%s, prefix=%s, acreg=%s, ata=%s, atd=%s, bay=%s, chk=%s,
    watersvc=%s, wastesvc=%s, afac=%s, gpu=%s, asu=%s, acu=%s, brk=%s, cherry=%s, platform=%s, pkg=%s, padd=%s, sadd=%s,
    nadd=%s, zadd=%s, cadd=%s, madd=%s, worked=%s, ovnbay=%s, tpc=%s, waterdrain=%s, wastedrain=%s, fueldrain=%s,
    stand=%s, wash=%s, mech1=%s, mech2=%s, eng=%s, tda=%s, fltrmk=%s, record=%s WHERE fltid=%s"""

flight_log = """SELECT fltid, DATE_FORMAT(arrdate, '%d %b %y'), airline, fltno, prefix, acreg, TIME_FORMAT(ata, '%H:%i')
    , TIME_FORMAT(atd, '%H:%i'), bay, chk 
    FROM flight
    ORDER BY fltid DESC
    LIMIT 300"""

count_h2osvc = """SELECT airline,
       COUNT(CASE WHEN MONTH(arrdate) = 1 THEN watersvc END)  AS 'JAN',
       COUNT(CASE WHEN MONTH(arrdate) = 2 THEN watersvc END)  AS 'FEB',
       COUNT(CASE WHEN MONTH(arrdate) = 3 THEN watersvc END)  AS 'MAR',
       COUNT(CASE WHEN MONTH(arrdate) = 4 THEN watersvc END)  AS 'APR',
       COUNT(CASE WHEN MONTH(arrdate) = 5 THEN watersvc END)  AS 'MAY',
       COUNT(CASE WHEN MONTH(arrdate) = 6 THEN watersvc END)  AS 'JUN',
       COUNT(CASE WHEN MONTH(arrdate) = 7 THEN watersvc END)  AS 'JUL',
       COUNT(CASE WHEN MONTH(arrdate) = 8 THEN watersvc END)  AS 'AUG',
       COUNT(CASE WHEN MONTH(arrdate) = 9 THEN watersvc END)  AS 'SEP',
       COUNT(CASE WHEN MONTH(arrdate) = 10 THEN watersvc END) AS 'OCT',
       COUNT(CASE WHEN MONTH(arrdate) = 11 THEN watersvc END) AS 'NOV',
       COUNT(CASE WHEN MONTH(arrdate) = 12 THEN watersvc END) AS 'DEC'
FROM flight
WHERE watersvc = 'YES'
GROUP BY airline"""

detail_h2osvc = """SELECT fltid, arrdate, airline, fltno, prefix, acreg, bay, watersvc
FROM flight
WHERE watersvc = 'YES'
ORDER BY fltid DESC"""

count_wastesvc = """SELECT airline,
       COUNT(CASE WHEN MONTH(arrdate) = 1 THEN watersvc END)  AS 'JAN',
       COUNT(CASE WHEN MONTH(arrdate) = 2 THEN watersvc END)  AS 'FEB',
       COUNT(CASE WHEN MONTH(arrdate) = 3 THEN watersvc END)  AS 'MAR',
       COUNT(CASE WHEN MONTH(arrdate) = 4 THEN watersvc END)  AS 'APR',
       COUNT(CASE WHEN MONTH(arrdate) = 5 THEN watersvc END)  AS 'MAY',
       COUNT(CASE WHEN MONTH(arrdate) = 6 THEN watersvc END)  AS 'JUN',
       COUNT(CASE WHEN MONTH(arrdate) = 7 THEN watersvc END)  AS 'JUL',
       COUNT(CASE WHEN MONTH(arrdate) = 8 THEN watersvc END)  AS 'AUG',
       COUNT(CASE WHEN MONTH(arrdate) = 9 THEN watersvc END)  AS 'SEP',
       COUNT(CASE WHEN MONTH(arrdate) = 10 THEN watersvc END) AS 'OCT',
       COUNT(CASE WHEN MONTH(arrdate) = 11 THEN watersvc END) AS 'NOV',
       COUNT(CASE WHEN MONTH(arrdate) = 12 THEN watersvc END) AS 'DEC'
FROM flight
WHERE wastesvc = 'YES'
GROUP BY airline"""

detail_wastesvc = """SELECT fltid, arrdate, airline, fltno, prefix, acreg, bay, wastesvc
FROM flight
WHERE wastesvc = 'YES'
ORDER BY fltid DESC"""

last = "SELECT fltid FROM flight ORDER BY fltid DESC LIMIT 1"
