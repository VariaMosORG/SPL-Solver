import asyncio

import nest_asyncio
import uvicorn
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .routers import mini_zinc, solvers, transformations

nest_asyncio.apply()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(solvers.router, prefix="/solvers", tags=["solvers"])
app.include_router(mini_zinc.router, prefix="/mini-zinc", tags=["mini_zinc"])
app.include_router(transformations.router, prefix="/transform", tags=["transform"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
