from fastapi import FastAPI
import posts


app = FastAPI()
app.include_router(posts.router)


@app.get("/")
def health_check():
    return {"message": "Hello World"}
