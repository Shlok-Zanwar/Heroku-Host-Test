import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from Routers import model_router
from pydantic import BaseModel

app = FastAPI()

router = APIRouter(
    tags=['Test']
)


@router.get('/')
def abc ():
    return 'Hello World'

# make a post route to add 2 numbers
@router.post('/add')
def add (a: int, b: int):
    return a + b

@router.get('/items/{item_id}')
def get_item(item_id: int, q: str = None):
    return {'item_id': item_id, 'q': q}

class ExampleSchema (BaseModel):
    num1: int
    num2: int
    operator: str

@router.post("/add-array")
def add_array(
    schema: ExampleSchema
):

    try:
        a = int(schema.num1)
        b = int(schema.num2)
    except:
        raise Exception('num1 and num2 should be numbers !')

    if schema.operator == '+':
        return a + b
    elif schema.operator == '-':
        return a - b
    elif schema.operator == '*':
        return a * b
    elif schema.operator == '/':
        return a / b
    else:
        return 'Invalid operator'


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

app.include_router(router)
app.include_router(model_router.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
