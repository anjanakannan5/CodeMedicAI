import sqlite3

def create_database():
    conn = sqlite3.connect("codemedic.db")
    curr = conn.cursor()
    try:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS error_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exception_type TEXT,
            error_message TEXT,
            line_number TEXT,
            file_name TEXT,
            source_code TEXT,
            full_source_code TEXT,
            traceback TEXT,
            timestamp TEXT
        );
        """
        curr.execute(create_table_query)
        conn.commit()
        #print("Table 'error_logs' created successfully!")

    except sqlite3.Error as err:
        print(f"An error occurred: {err}")
    finally:
        conn.close()

def save_error(analysis):
    print("[Database ]")
    print("→ Saving error log...")
    conn = sqlite3.connect("codemedic.db")
    curr = conn.cursor()
    try:
        insert_log = (
            analysis["exception_type"],
            analysis["error_message"],
            analysis["line_number"],
            analysis["file_name"],
            analysis["source_code"],
            analysis["full_source_code"],
            analysis["traceback"],
            analysis["timestamp"],
        )
        curr.execute(
            "INSERT INTO error_logs (exception_type, error_message, line_number, file_name, source_code, full_source_code, traceback, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            insert_log,
        )
        print("✓ Error log saved.\n")
        conn.commit()
    except sqlite3.Error as err:
        print(f"An error occurred: {err}")
    finally:
        conn.close()