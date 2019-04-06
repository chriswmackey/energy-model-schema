from pydantic import BaseModel, Schema, UrlStr
from uuid import UUID

additional_error_post_responses = {
    401: {"description": "Unauthorized"},
    403: {"description": "Access forbidden"},
    500: {"description": "Server error"}
}

additional_error_responses = {
    **additional_error_post_responses,
    404: {"description": "Not found"}
}


created_header_schema = {
    'Location': {
        'description': 'Location of the newly created resource.',
        'schema': {
            'type': 'string', 'format': 'url'
        }
    }
}


class CreatedContent(BaseModel):
    """Content for created response."""
    id: UUID = Schema(
        ...,
        description='Id for the newly created resource.',
        example='3fa85f64-5717-4562-b3fc-2c963f66afa6'
    )
    message: str = Schema(
        None,
        description=' A human readable message',
        example='Use Location in headers to access the new object.'
    )
