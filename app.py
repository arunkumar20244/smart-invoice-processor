import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Smart-Invoice-Processor")

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "Smart-Invoice-Processor"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
