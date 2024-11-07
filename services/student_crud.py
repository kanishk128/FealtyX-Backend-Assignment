from models.student import StudentCreate
from fastapi import HTTPException, status
import requests
import json

students={}

def create_stud(student:StudentCreate):
    stud=students.get(student.ID)
    if stud:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Student with ID already exists")
    students[student.ID]=student
    return student

def get_studs():
    li=[
        {
            "ID":student.ID,
            "Name":student.Name,
            "Age":student.Age,
            "Email":student.Email
        }
        for student in students.values()
    ]
    return li

def get_stud(id:int):
    return students.get(id)

def update_stud(id:int, student:StudentCreate):
    if student.ID != id and student.ID in students:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="New ID already taken")
    students[id] = student  # Update the student record or create a new one if it doesn't exist
    return student

def del_stud(id:int):
    #Will return True if there exists a student by id and successfully deleted, false otherwise
    stud=get_stud(id)
    if stud:
        del students[id]
        return True
    return False

#API URL of Ollama for generating summary    
url="http://localhost:11434/api/generate"
headers={
    'Content-Type':"application/json"
}

def generate_summary(id:int):

    stud=get_stud(id)
    
    if not stud:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {id} not found"
        )

    data={
        "model":"llama3.1",
        "prompt":f"Generate a brief sumary of this student data in a single sentence {stud},",
        "stream": False
    }
    
    try:
        response=requests.post(url,headers=headers,data=json.dumps(data))
        if response.status_code==200: 
            data=response.json()
            summary=data.get('response','').strip()
            return summary.rsplit("\n", 1)[-1] if summary else None
        
    except requests.exceptions.RequestException as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Summary generation failed due to an external service error"
            )