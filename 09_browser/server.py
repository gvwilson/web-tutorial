"""Color server."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random


def make_server():
    """Build application and configure routes."""
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/")
    def root():
        return {
            "red": random.randint(0, 255),
            "green": random.randint(0, 255),
            "blue": random.randint(0, 255),
        }

    return app

app = make_server()
