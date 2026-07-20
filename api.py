from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="AEGIS API",
    version="1.0.0"
)


@app.get("/")
def root():

    return {

        "service": "AEGIS",

        "version": "1.0.0",

        "status": "online"

    }


@app.get("/health")
def health():

    return {

        "status": "ok"

    }


@app.get("/radar")
def radar():

    return JSONResponse(

        content={

            "message": "Radar todavía no conectado"

        }

    )