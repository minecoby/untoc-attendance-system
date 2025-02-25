from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Club Attendance System API is running with Conda!"}
