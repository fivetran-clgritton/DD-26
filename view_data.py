import duckdb

conn = duckdb.connect("files/warehouse.db", read_only=True)

tables = [t for (t,) in conn.execute(
    "SELECT table_name FROM information_schema.tables WHERE table_schema = 'tester'"
).fetchall()]

for t in tables:
    count = conn.execute(f"SELECT COUNT(*) FROM tester.{t}").fetchone()[0]
    print(f"\n=== {t} ({count} rows) ===")
    print(conn.execute(f"SELECT * FROM tester.{t} LIMIT 3").fetchdf().to_string())
