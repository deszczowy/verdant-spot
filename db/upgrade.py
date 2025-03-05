import sqlite3
import os
from .client import DbBaseClient

class DbUpgrader(DbBaseClient):

    CHANGES_SOURCE = "db/changes/"

    def __init__(self, db_path: str) -> None:
        super().__init__(db_path)

    def _service_table_exists(self) -> bool:
        try:
            with sqlite3.connect(self.db_path) as conn:
                result = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='service'")
                return result.fetchone() is not None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return False

    def _get_current_version(self) -> int:
        if not self._service_table_exists():
            try:
                with sqlite3.connect(self.db_path) as conn:
                    conn.execute("CREATE TABLE service (version INTEGER PRIMARY KEY, description TEXT)")
                    conn.commit()
                    return 0
            except sqlite3.Error as e:
                print(f"Database error: {e}")
                return 0

        try:
            with sqlite3.connect(self.db_path) as conn:
                version = conn.execute("SELECT MAX(version) FROM service").fetchone()[0]
                return version if version else 0
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return 0        

    def upgrade(self) -> None:
        version = self._get_current_version()
        change_scripts = sorted(
            [f for f in os.listdir(self.CHANGES_SOURCE) if f.endswith(".sql")],
            key=lambda x: int(x.split("-")[0])
        )

        for script in change_scripts:
            script_data = script.split("-")
            
            script_id = int(script_data[0])
            script_name = script_data[1]

            if script_id > version:
                with open(os.path.join(self.CHANGES_SOURCE, script), "r") as f:
                    sql = f.read()
                print(f"Upgrade by {script}...")

                with sqlite3.connect(self.db_path) as conn:
                    try:
                        conn.executescript(sql)
                        conn.execute("INSERT INTO service (version, description) VALUES (?, ?)", (script_id, script_name,))
                        conn.commit()
                    except sqlite3.Error as e:
                        print(f"Upgrade error, caused by {script}: {e}")
                        conn.rollback()
                        return