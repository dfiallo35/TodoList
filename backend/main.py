from fastapi import FastAPI


app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")


@app.get("/")
async def read_root():
    return {"message": "Hello World"}