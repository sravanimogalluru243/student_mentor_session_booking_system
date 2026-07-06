from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.connection import engine, Base

from app.models import admin, student, mentor, session, booking, feedback
from app.api import booking, mentor, session, feedback, auth, student, admin


def create_app() -> FastAPI:
    app = FastAPI(title="Student-Mentor Booking")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "http://127.0.0.1:5173",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth.router)
    app.include_router(mentor.router)
    app.include_router(session.router)
    app.include_router(booking.router)
    app.include_router(feedback.router)
    app.include_router(student.router)
    app.include_router(admin.router)

    return app


app = create_app()


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)