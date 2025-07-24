import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.exc import SQLAlchemyError
from starlette.middleware.errors import ServerErrorMiddleware
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

import database
from routers import permits, users  # Assuming you'll create these routers

app = FastAPI(title="Government Permit Management System", version="1.0.0", openapi_url="/openapi.json")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Replace with your allowed origins in production
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

#Error Handling Middleware
app.add_middleware(ServerErrorMiddleware, handler=lambda _: JSONResponse(status_code=HTTP_500_INTERNAL_SERVER_ERROR, content={'detail': 'Internal Server Error'}))

# Database Initialization
database.Base.metadata.create_all(bind=database.engine)

# Router Registration
app.include_router(permits.router)
app.include_router(users.router)

# Health Check Endpoint
@app.get('/health')
def health_check():
    return {'status': 'ok'}

# Serve static files for frontend
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")
    
    @app.get("/{{"file_path:path}}")
    async def serve_frontend(file_path: str, request:Request):
        if file_path.startswith("api"):
            return None #Let API routes handle it
        static_file = os.path.join("static", file_path)
        if os.path.isfile(static_file):
            return FileResponse(static_file)
        return FileResponse("static/index.html") #SPA Routing

@app.exception_handler(SQLAlchemyError)
def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    return JSONResponse(status_code=500, content={'detail': f'Database error: {str(exc)}'})

