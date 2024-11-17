from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from routers import operaciones

URL_DOCUMENTATION = "/docs"

app = FastAPI(docs_url=URL_DOCUMENTATION, redoc_url=None)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Redirect to documentation
@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url=URL_DOCUMENTATION)


# Import routers
app.include_router(operaciones.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=9000)
