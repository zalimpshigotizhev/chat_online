from fastapi import FastAPI

def create_app():
    app = FastAPI(
        title="Simple Kafka Chat",
        docs_url="/api/docs/",
        description="A simple kafka + ddd example",
        debug=True,
    )
    return app