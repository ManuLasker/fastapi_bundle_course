from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
from typing import Optional

api = FastAPI()

@api.get("/")
def index():
    body = "<html>" \
            "<body style='padding:10px;'>" \
            "<h1> Welcome to the API!</h1>" \
            "<div>" \
            "Try it: <a href='/api/calculate?x=7&y=11'> /api/calculate?x=7&y=11 </a>" \
            "</div>" \
            "</body>" \
            "</html>"
    return HTMLResponse(body)

@api.get("/api/calculate")
def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": "Cannot devide by 0"},
        )
    value:float = x + y
    if z is not None:
        value = value/z
    return {"value": value}
