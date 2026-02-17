import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.app.interface.strawberry.router import get_strawberry_graphql_router
from src.app.interface.fastapi.middleware.hmac import verify_hmac
from src.security.domain.exceptions import HMACException
from src.di.injector import Injector
from src.app.setup import setup_dependencies

logger = logging.getLogger(__name__)

def lifespan(app: FastAPI):
    api_injecor = Injector()
    setup_dependencies(injector=api_injecor)
    app.state.injector = api_injecor
    yield

def create_fastapi_app():
    app = FastAPI(lifespan=lifespan)

    # CORS setup
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:4200", "http://localhost:8000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

        
    @app.exception_handler(HMACException)
    async def hmac_exception_handler(request, exc: HMACException):
        return JSONResponse(
            status_code=403,
            content={"errors": [exc.detail]}
        )


    @app.exception_handler(Exception)
    async def exception_handler(request, exc: Exception):
        print(str(exc))
        return JSONResponse(
            status_code=500,
            content={"errors": ["Unable to process request at this time"]}
        )


    @app.get("/", tags=["Internal"])
    async def health():
        """
        ## Health check 
        This endpoints verifies server status.
        """
        return {"status": "Renters ok"}
    
  
    # graphql_router = get_strawberry_graphql_router()
    # app.include_router(graphql_router, dependencies=[Depends(verify_hmac)])

    return app
    
    