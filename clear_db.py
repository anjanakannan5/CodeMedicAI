import sqlite3
conn = sqlite3.connect("codemedic.db")
curr = conn.cursor()
curr.execute("DROP TABLE error_logs")