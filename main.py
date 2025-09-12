from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from pymongo import MongoClient
from datetime import date, datetime

# MongoDB connection
MONGO_URI = // paste your mongodb connection string here 
client = MongoClient(MONGO_URI)
db = client["employee_db"]
employees_collection = db["employees"]

app = FastAPI()

# Pydantic schemas
class Employee(BaseModel):
    employee_id: str
    name: str
    department: str
    salary: float
    joining_date: date
    skills: List[str]

class UpdateEmployee(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[float] = None
    joining_date: Optional[date] = None
    skills: Optional[List[str]] = None

# Helper function to convert date to datetime for MongoDB
def date_to_datetime(d: date) -> datetime:
    return datetime.combine(d, datetime.min.time())

# Create Employee
@app.post("/employees")
def create_employee(employee: Employee):
    if employees_collection.find_one({"employee_id": employee.employee_id}):
        raise HTTPException(status_code=400, detail="Employee ID already exists")
    employee_dict = employee.dict()
    employee_dict["joining_date"] = date_to_datetime(employee.joining_date)
    employees_collection.insert_one(employee_dict)
    return {"message": "Employee created successfully"}
# Average Salary by Department
@app.get("/employees/avg-salary")
def average_salary():
    pipeline = [
        {"$group": {"_id": "$department", "avg_salary": {"$avg": "$salary"}}},
        {"$project": {"department": "$_id", "avg_salary": 1, "_id": 0}}
    ]
    result = list(employees_collection.aggregate(pipeline))
    return result
# Search Employees by Skill
@app.get("/employees/search")
def search_by_skill(skill: str):
    employees = list(employees_collection.find(
        {"skills": skill},
        {"_id": 0}
    ))
    return employees
    
# Get Employee by ID

@app.get("/employees/{employee_id}")
def get_employee(employee_id: str):
    employee = employees_collection.find_one({"employee_id": employee_id}, {"_id": 0})
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

# Update Employee (partial update allowed)
@app.put("/employees/{employee_id}")
def update_employee(employee_id: str, updates: UpdateEmployee):
    update_data = {k: v for k, v in updates.dict().items() if v is not None}
    # Convert joining_date if present
    if "joining_date" in update_data:
        update_data["joining_date"] = date_to_datetime(update_data["joining_date"])
    result = employees_collection.update_one(
        {"employee_id": employee_id},
        {"$set": update_data}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee updated successfully"}


# Delete Employee
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: str):
    result = employees_collection.delete_one({"employee_id": employee_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}

# List Employees by Department
@app.get("/employees")
def list_by_department(department: str):
    employees = list(employees_collection.find(
        {"department": department},
        {"_id": 0}
    ).sort("joining_date", -1))
    return employees



