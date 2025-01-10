from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
import uvicorn

from inbrief.controllers.youtube_controller import router as YoutubeRouter

app = FastAPI()
app.include_router(YoutubeRouter)


@app.get("/")
def index():
    return {"Hello": "World"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

    