import os
import asyncpg
from asyncpg.connection import Connection
from fastapi import HTTPException


async def get_database_connection() -> Connection:
    try:
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise HTTPException(
                status_code=500, detail="DATABASE_URL environment variable is not set"
            )

        conn = await asyncpg.connect(database_url)
        return conn
    except asyncpg.exceptions.PostgresError as e:
        raise HTTPException(
            status_code=500, detail=f"Database connection error: {str(e)}"
        )
