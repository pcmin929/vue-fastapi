from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    response = {
        'data': [
            {
                'id': 1,
                'name': 'Chocolate',
                'price': '4.50',
            },
            {
                'id': 2,
                'name': 'Sorvete',
                'price': '2.42',
            },
            {
                'id': 3,
                'name': 'Refrigerante',
                'price': '4.90',
            },
            {
                'id': 4,
                'name': 'X-salada',
                'price': '7.99',
            },
        ]
    }
    return response


if __name__ == '__main__':
    from uvicorn import run
    run("main:app", reload=True)
  