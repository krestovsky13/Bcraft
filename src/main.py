from fastapi import FastAPI

from bcraft.api.routes import router
from bcraft.config import settings


def start_application():
    """
    Инициализация приложения
    """
    app = FastAPI(
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        version=settings.PROJECT_VERSION,
    )

    app.include_router(router, prefix='/api/v1')

    return app


app = start_application()


@app.get('/')
def main():
    """
    Main endpoint
    """
    return {
        'app': 'Bcraft microservice for statistics counters API',
        'doc_path': '/docs',
        'redoc_path': '/redoc',
    }
