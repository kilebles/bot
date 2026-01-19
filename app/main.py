import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.database import Base, engine
from app.handlers import get_main_router
from app.models import User  # noqa: F401
from app.settings import settings


async def on_startup() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    await on_startup()

    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()

    dp.include_router(get_main_router())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
