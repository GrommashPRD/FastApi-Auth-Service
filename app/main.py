from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

#Auth
from app.api.handlers.auth.router import router as authorization_router
#Profile
from app.api.handlers.users.router import router as profile_router


app = FastAPI()

app.include_router(authorization_router)
app.include_router(profile_router)

@app.get("/ping", response_class=PlainTextResponse)
async def ping():
    return "pong"
