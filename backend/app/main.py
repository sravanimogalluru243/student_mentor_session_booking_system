from fastapi import FastAPI
from app.database.connection import engine, Base

# 👇 IMPORTANT: import ALL models
from app.models import admin, student, mentor, session, booking, feedback

from app.api import booking, mentor, session, feedback, auth, student, admin


def create_app() -> FastAPI:
    app = FastAPI(title="Student-Mentor Booking")

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