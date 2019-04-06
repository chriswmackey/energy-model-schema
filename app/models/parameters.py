"""Reusable parameters."""
from fastapi import Query

per_page_param = Query(
    25,
    alias='per-page',
    title='Items per page',
    description='Number of items per page',
    le=100
)

page_param = Query(
    1,
    title='Page number',
    description='Page number starting from 1',
    ge=1
)
