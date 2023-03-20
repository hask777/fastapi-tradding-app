from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.types import TIMESTAMP

metadata = MetaData()

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantity", String),
    Column("figi", String),
    Column("instrument_type", String, nullable=True),
    Column("date", type_=TIMESTAMP(timezone=True)),
    Column("type", String),
)
