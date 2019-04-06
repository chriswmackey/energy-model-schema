from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from starlette.middleware.cors import CORSMiddleware
from app.core.config import ALLOWED_HOSTS, PROJECT_NAME

from app.api.endpoints import router as api_router


# create the app
app = FastAPI(title=PROJECT_NAME)

if not ALLOWED_HOSTS:
    ALLOWED_HOSTS = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# add endpoints to app
app.include_router(api_router)


# customize openapi documentation
def custom_openapi():
    """Customize openapi documentation page."""
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="pollination.cloud",
        version="0.0.1",
        description="This page only documents %s endpoints."
        " See the link below for full API documentation." % PROJECT_NAME,
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://user-images.githubusercontent.com/2915573/53690998-7239bb00-3d43-11e9-85b1-d9ac9d140c0f.png"
    }

    openapi_schema["info"]["license"] = {
        "name": "AGPL",
        "url": "https://www.gnu.org/licenses/agpl-3.0.en.html"
    }

    openapi_schema["externalDocs"] = {
        "description": "Pollination Cloud full API documentation.",
        "url": "https://pollination.cloud/api"
    }

    # openapi_schema["servers"] =  [{"url": "http://api.pollination.cloud"}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
