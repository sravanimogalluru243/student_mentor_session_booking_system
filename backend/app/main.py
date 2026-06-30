from fastapi import FastAPI

from app.database.connection import engine, Base
from app.api import booking, mentor, session, feedback, auth


def create_app() -> FastAPI:
    app = FastAPI(title="Student-Mentor Booking")

    app.include_router(auth.router)
    app.include_router(mentor.router)
    app.include_router(session.router)
    app.include_router(booking.router)
    app.include_router(feedback.router)

    return app


app = create_app()


@app.on_event("startup")
def on_startup():
    # create tables for local development (SQLite)
    Base.metadata.create_all(bind=engine)
