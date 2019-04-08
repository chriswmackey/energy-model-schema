from fastapi import APIRouter, Query, Path, Body, HTTPException, Depends
from fastapi.openapi.utils import get_openapi
from uuid import UUID
from typing import List

from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_200_OK
from starlette.responses import JSONResponse, HTMLResponse

# model libraries
from app.models.schemas import Face, Model, ModelOut

from app.models.responses import (
    created_header_schema, CreatedContent, paging_header_schema,
    additional_error_post_responses, additional_error_responses
)
from app.models.security import User
from app.core.jwt import get_user_info
from app.core.config import HOST_NAME

# TODO(): change input parameters to dependency
from app.models.parameters import per_page_param, page_param
from app.crud.database import (create_model_db, get_models_db, get_model_db, 
    delete_model_db, get_faces_db, create_faces_db, count_models_db
)

from app.models.samples.model import model_sample

from app.crud.util import generate_paging_link 

router = APIRouter()

@router.get(
    "/",
    operation_id='models_welcome',
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
    responses={
        **additional_error_responses,
        200: {
            'headers': paging_header_schema
        }
    })
def get_models(
    page: int = page_param,
    per_page: int = per_page_param,
    user: User = Depends(get_user_info)
):
    """Retrieve a list of models."""
    link = 'http://%s/models' % (HOST_NAME)
    total_count = count_models_db(user)
    models = get_models_db(page, per_page, user)
    header_links = generate_paging_link(link, page, total_count, per_page) 
    return JSONResponse(
        status_code=200,
        headers={'Link': str(header_links)},
        content=[model.to_model_out() for model in models]
    )


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
        example = model_sample),
    user: User = Depends(get_user_info)
):
    """Create a new model."""
    nid = create_model_db(model, user)
    location = '%s/models/%s' % (HOST_NAME, nid)
    return JSONResponse(
        status_code=201,
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
    return ModelOut.parse_obj(get_model_db(id, user).to_model_out())



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
    link = 'http://%s/models' % (HOST_NAME)
    faces, face_count = get_faces_db(id, page, per_page, user)
    links = generate_paging_link(link, page, face_count, per_page)
    return JSONResponse(
        status_code=200,
        headers={'Link': str(links)},
        content= [face.to_face_out() for face in faces]
    )

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
    faces: List[Face] = Body(
        ...,
        description = "A list of Pollination model faces",
        title = "Faces",
        example = model_sample['faces']),
    user: User = Depends(get_user_info)
):
    """Create new model faces."""
    nids = create_faces_db(id, faces, user)
    location = '%s/models/%s/faces' % (HOST_NAME, nids)
    return JSONResponse(
        status_code=201,
        headers={'Location': location},
        content={
            'ids': nids,
            'message': 'Use Location in headers to access the new object.'
        }
    )