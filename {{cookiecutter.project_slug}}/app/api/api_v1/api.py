from fastapi import APIRouter
from meilisearch_fastapi.routes import (
    document_routes,
    index_routes,
    meilisearch_routes,
    search_routes,
    settings_routes,
)

api_router = APIRouter()
api_router.include_router(document_routes.router, prefix="/meilisearch/documents")
api_router.include_router(index_routes.router, prefix="/meilisearch/indexes")
api_router.include_router(meilisearch_routes.router, prefix="/meilisearch")
api_router.include_router(search_routes.router, prefix="/search")
api_router.include_router(settings_routes.router, prefix="/meilisearch/settings")
