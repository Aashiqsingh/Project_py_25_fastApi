from fastapi import FastAPI

app = FastAPI()

@app.get("/test/")
async def test():
    return "Hii baby..."


@app.get("/demo/")
async def demo():
    return {
        "message":"demo function called...",
        "status":102
    }