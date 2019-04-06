from fastapi import APIRouter, Query, Path, Body, HTTPException, Depends
from fastapi.openapi.utils import get_openapi
from uuid import UUID
from typing import List

from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_200_OK
from starlette.responses import JSONResponse, HTMLResponse

# model libraries
from app.models.schemas import Face, Model, ModelOut

from app.models.responses import (
    created_header_schema, CreatedContent,
    additional_error_post_responses, additional_error_responses
)
from app.models.security import User
from app.core.jwt import get_user_info

# TODO(): change input parameters to dependency
from app.models.parameters import per_page_param, page_param
from app.crud.database import (create_model_db, get_models_db, get_model_db, 
    delete_model_db, get_faces_db, create_faces_db
)

HOST = 'https://api.pollination.cloud'

router = APIRouter()

@router.get(
    "/",
    operation_id='sensor_grids_welcome',
    include_in_schema=False,
    content_type=None
)
def say_hi_models():
    """Landing page."""
    response = HTMLResponse(
        '<html><body>'
        '<h1>Welcome!</h1>'
        '<h2>See the interactive <a href="/docs">API documentation</a></h2>'
        '<h2>See the redoc <a href="/redoc">API documentation</a></h2>'
        '</body></html>'
    )
    return response

@router.get(
    "/models/",
    operation_id='get_models',
    tags=['Model'],
    summary='Get Models',
    status_code=HTTP_200_OK,
    response_description='Retrieved',
    response_model=List[ModelOut],
    responses={**additional_error_responses}
)
def get_models(
    page: int = page_param,
    per_page: int = per_page_param,
    user: User = Depends(get_user_info)
):
    """Retrieve a list of sensor grids."""
    models = get_models_db(page, per_page, user)
    return [
        ModelOut.parse_obj(model.to_model_out(HOST)) for model in models
        ]


@router.post(
    "/models/",
    operation_id='create_model',
    tags=['Model'],
    summary='Create a Model',
    status_code=HTTP_201_CREATED,
    response_description='Created successfully',
    response_model=CreatedContent,
    responses={
        **additional_error_post_responses,
        201: {
            'headers': created_header_schema
        }
    }
)
def create_model(
    model: Model = Body(
        ...,
        description = "A Pollination model",
        title = "Model",
        example = {}), # TODO(): Add model example
    user: User = Depends(get_user_info)
):
    """Create a new model."""
    nid = create_model_db(model, user)
    location = '%s/models/%s' % (HOST, nid)
    return JSONResponse(
        headers={'Location': location},
        content={
            'id': nid,
            'message': 'Use Location in headers to access the new object.'
        }
    )

@router.get(
    "/models/{id}",
    operation_id='get_model',
    tags=['Model'],
    summary='Get a Model',
    status_code=HTTP_200_OK,
    response_description='Retrieved',
    response_model=ModelOut,
    responses={**additional_error_responses}
)
def get_model(
    id: UUID = Path(..., title = "Model id."),
    user: User = Depends(get_user_info)
):
    """Retrieve a sensor grid."""
    return ModelOut.parse_obj(get_model_db(id, user).to_model_out(HOST))



@router.delete(
    "/models/{id}",
    operation_id='del_model',
    tags=['Model'],
    summary='Delete a Model',
    status_code=HTTP_204_NO_CONTENT,
    response_description='Success',
    responses={**additional_error_responses}
)
def delete_model(
    id: UUID = Path(
        ...,
        title = "Model id",
        description = "Model id."),
    user: User = Depends(get_user_info)
):
    """Delete a sensor grid."""
    delete_model_db(id, user)

@router.get(
    "/models/{id}/faces",
    operation_id='get_faces',
    tags=['Model'],
    summary='Get Model Faces',
    status_code=HTTP_200_OK,
    response_description='Retrieved',
    response_model=List[Face],
    responses={**additional_error_responses}
)
def get_faces(
    id: UUID = Path(..., title = "model id."),
    page: int = page_param,
    per_page: int = per_page_param,
    user: User = Depends(get_user_info)
):
    """Retrieve list of sensors for a sensor grid.
    See Location in response headers for paging links.
    """
    faces = get_faces_db(id, page, per_page, user)
    return [Face.parse_obj(face.to_face_out()) for face in faces]


@router.post(
    "/models/{id}/faces",
    operation_id='create_faces',
    tags=['Model'],
    summary='Create Model Faces',
    status_code=HTTP_201_CREATED,
    response_description='Created successfully',
    response_model=CreatedContent,
    responses={
        **additional_error_post_responses,
        201: {
            'headers': created_header_schema
        }
    }
)
def create_faces(
    model: List[Face] = Body(
        ...,
        description = "A list of Pollination model faces",
        title = "Faces",
        example = {}), # TODO(): Add model example
    user: User = Depends(get_user_info)
):
    """Create new model faces."""
    nids = create_faces_db(model, user)
    location = '%s/models/%s/faces' % (HOST, nids)
    return JSONResponse(
        headers={'Location': location},
        content={
            'ids': nids,
            'message': 'Use Location in headers to access the new object.'
        }
    )