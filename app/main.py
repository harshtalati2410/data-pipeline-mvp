from fastapi import FastAPI
from app.api.routes import router
from app.core.processor import run_user_script

app = FastAPI()
app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}

dummy_script = """
def process(data):
    for row in data:
        row["value"] *= 2
    return data
"""

sample_data = [{"value": 10}, {"value": 20}]

@app.post("/run-script")
def run_script(script: str | None = dummy_script, data: list | None= sample_data):
    try:
        result = run_user_script(script, data)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
