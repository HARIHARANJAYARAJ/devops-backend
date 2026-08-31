from sqlalchemy import inspect, text
from sqlalchemy.sql.sqltypes import (
    String,
    Integer,
    Date,
    Boolean,
    Float,
)


def sync_database_schema(engine, Base):
    """
    Automatically add missing columns from SQLAlchemy models.

    This is intended for additive schema changes.
    It does NOT automatically drop or rename existing columns.
    """

    inspector = inspect(engine)

    for table_name, table in Base.metadata.tables.items():

        # Create the table if it doesn't exist.
        if not inspector.has_table(table_name):
            table.create(bind=engine)
            print(f"[SCHEMA] Created table: {table_name}")
            continue

        existing_columns = {
            column["name"]
            for column in inspector.get_columns(table_name)
        }

        for column in table.columns:

            if column.name in existing_columns:
                continue

            column_type = column.type

            if isinstance(column_type, String):
                sql_type = f"VARCHAR({column_type.length or 255})"

            elif isinstance(column_type, Integer):
                sql_type = "INTEGER"

            elif isinstance(column_type, Date):
                sql_type = "DATE"

            elif isinstance(column_type, Boolean):
                sql_type = "BOOLEAN"

            elif isinstance(column_type, Float):
                sql_type = "DOUBLE PRECISION"

            else:
                raise RuntimeError(
                    f"Unsupported automatic column type: "
                    f"{table_name}.{column.name} "
                    f"({column_type})"
                )

            nullable = "" if column.nullable else " NOT NULL"

            sql = f"""
                ALTER TABLE {table_name}
                ADD COLUMN {column.name} {sql_type}{nullable}
            """

            with engine.begin() as connection:
                connection.execute(text(sql))

            print(
                f"[SCHEMA] Added column: "
                f"{table_name}.{column.name} {sql_type}"
            )