import sqlite3

class DbBaseClient:

    def __init__(self, db_path: str) -> None:
        """
        SQLite client initialisation
        :param db_path: db file path
        """
        self.db_path = db_path

    def execute_select(self, query: str, params: tuple = ()) -> list[dict]:
        """
        Performs a query based on given params and returns the results as a list of dictionaries.
        : Param Query: SQL query (should be select type).
        : Param Params: Optional parameters to ask.
        : Return: List of dictionaries, where the key is the name of the column.
        """
        results = []
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(query, params)
                rows = cursor.fetchall()
                results = [dict(row) for row in rows]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return results
