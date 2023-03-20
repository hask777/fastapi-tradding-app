from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
import json
import datetime

from src.database import get_async_session
from src.operations.models import operation
from src.operations.schemas import OperationCreate

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)

    return [dict(data._mapping) for data in result]


@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    # for op in new_operation.dict():
    #     print(op)
    # print(new_operation.id)
    # stmt = insert(operation).values(id=2233, quantity='fg', figi='45', instrument_type='fg', date=datetime.datetime.now(), type='dfd')
    # print(stmt)

    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

"""
2023-03-18T13:42:28.123Z

2023-03-18T14:02:35.224Z
"""

