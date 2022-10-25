from secao4.core.configs import settings
from secao4.core.database import engine


async def creat_tables() -> None:
    import models.__all_models
    print("Creating tables...")

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print("Tables created!")


if __name__ == "__main__":
    import asyncio
    asyncio.run(creat_tables())