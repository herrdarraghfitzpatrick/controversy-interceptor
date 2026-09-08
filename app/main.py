from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.routers import library, scan

settings = get_settings()

app = FastAPI(
    title="Controversy Scanner API",
    description="Scans campaign text/briefs for phrases, imagery, or concepts "
    "that could trigger a cultural, political, historical, or social-media "
    "backlash in a given target market.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(scan.router)
app.include_router(library.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
