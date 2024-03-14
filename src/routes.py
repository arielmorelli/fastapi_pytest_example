from fastapi import FastAPI, APIRouter


def hello_world_route() -> APIRouter:
    """Hello World! route.

    Check: https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter

    Returns: APIRouter
    """
    router = APIRouter()

    @router.get("/hello-world")
    def hello():
        return {"hello": "world"}

    return router


def create_routes(app: FastAPI) -> None:
    """Add routers to app.

    Args:
        app: FastAPI instance
    """
    app.include_router(hello_world_route())
