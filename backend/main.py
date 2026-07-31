from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Kirti API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

students_db = []

@app.get("/")
def root():
    return {"name": "Kirti API", "status": "running", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/api/students")
def get_students():
    return {"students": students_db}

@app.post("/api/students")
def create_student(name: str, grade: str):
    new_student = {"id": len(students_db) + 1, "name": name, "grade": grade}
    students_db.append(new_student)
    return {"status": "success", "student": new_student}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)