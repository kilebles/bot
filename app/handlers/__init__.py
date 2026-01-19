from aiogram import Router

from app.handlers import start


def get_main_router() -> Router:
    router = Router()
    router.include_router(start.router)
    return router
