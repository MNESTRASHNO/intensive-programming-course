#  uvicorn main:app --port 8080


from typing import Annotated
from fastapi import Depends, FastAPI, Form, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Func


app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/all_func")
def all_functions(
    db: Annotated[Session, Depends(get_db)],
):
    functions = db.scalars(
        select(Func)
    ).all()

    return [
        {
            "id": function.id,
            "func_name": function.func_name,
            "func_code": function.func,
        }
        for function in functions
    ]


@app.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
)
def create_func(
    name: Annotated[str, Form()],
    func_code: Annotated[str, Form()],
    db: Annotated[Session, Depends(get_db)],
):
    new_function = Func(
        func_name=name,
        func=func_code,
    )

    db.add(new_function)
    db.commit()
    db.refresh(new_function)

    return {
        "id": new_function.id,
        "func_name": new_function.func_name,
        "func_code": new_function.func,
    }

@app.get("/run/{func_id}", status_code=200)
async def run(
    func_id: int,
    db: Annotated[Session, Depends(get_db)],
):
    result = db.get(Func, func_id)

    if result is None:
        return {"error": "Функция не найдена"}

    namespace = {}

    exec(result.func, namespace)

    function = namespace[result.func_name]
    function_result = function()

    return {"result": function_result}

