from fastapi import FastAPI, HTTPException, status
from models.student import StudentCreate
from services.student_crud import create_stud, get_studs, get_stud, update_stud, del_stud, generate_summary
from fastapi.responses import JSONResponse

app=FastAPI()

#Dictionary to store student details
students={} #id->student object

@app.get("/")
async def welcome_func():
        return {
        "message": '''Welcome to FealtyX Backend Assignment by Kanishk Singhal
Email: singhalkanishk68@gmail.com
Mobile No.: 9717411578'''
    }

#API-1: Create a new student
@app.post("/students")
async def create_student(student:StudentCreate):
    try:
        student = create_stud(student)
        return {"status": "success", "message": f"Student with ID#{student.ID} added", "data": student}
    except HTTPException as e:
        if e.status_code == status.HTTP_409_CONFLICT:
            return JSONResponse(
                status_code=status.HTTP_409_CONFLICT,
                content={"status": "error", "message": "Student with ID already exists", "data": None}
            )
    # raise HTTPException(status_code=405,detail="Student with ID already exists")

#API-2: Get all students
@app.get("/students")
async def get_students():

    li=get_studs()

    if len(li):
        return {"status":"success","message":"","data":li}
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"status": "error", "message": "No student records", "data": None}
        )


#API-3: Get a student by ID
@app.get("/students/{id}")
async def get_student(id:int):
    student = get_stud(id)
    if student:
        return {"status": "success", "message": "", "data": student}
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"status": "error", "message": "Student not found!", "data": None}
        )


#API-4: Update a student by ID
@app.put("/students/{id}")
async def update_student(id:int,student:StudentCreate):
    try:
        student = update_stud(id, student)
        return {"status": "success", "message": "Updated student record", "data": student}
    except HTTPException as e:
        if e.status_code == status.HTTP_409_CONFLICT:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="New ID already taken")


#API-5: Delete a student by ID
@app.delete("/students/{id}")
async def delete_student(id:int):
    status=del_stud(id)
    if status:
        return {"status":"success","message":"Deleted Student","data":None}
    
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"status": "error", "message": "No student record", "data": None}
    )


#API-6: Generate summary of student by ID using Ollama
@app.get("/students/{id}/summary")
async def student_summary(id:int):
    try:
        summary = generate_summary(id)
        if summary:
            return {"status": "success", "message": "", "data": summary}
    except HTTPException as e:
        # If student not found, raise the 404 error 
        if e.status_code == status.HTTP_404_NOT_FOUND:
            raise e
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Summary generation failed due to an external service error"
        )