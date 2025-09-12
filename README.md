# FastAPI Employee Management System

A RESTful API built with FastAPI and MongoDB Atlas for managing employee data with features like CRUD operations, skill-based search, and department analytics.

## 🚀 Features

- Create, read, update, and delete employees
- Search employees by skills
- Calculate average salary by department
- List employees by department (sorted by joining date)
- Full data validation with Pydantic
- MongoDB Atlas integration

## 📋 Prerequisites
- A MongoDB Atlas account (free tier available)

## 🛠️ Installation Guide

### Step 1: Install Python

#### Windows:
1. Go to [python.org](https://www.python.org/downloads/)
2. Download Python 3.8 or higher
3. Run the installer and **check "Add Python to PATH"**
4. Verify installation: open Command Prompt and type `python --version`

#### macOS:
```bash
# Using Homebrew (recommended)
brew install python3

# Or download from python.org
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Step 2: Verify pip Installation

Pip comes with Python 3.4+. Verify it's installed:
```bash
pip --version
# or
pip3 --version
```

If pip is missing, install it:
```bash
python -m ensurepip --upgrade
```

### Step 3: Set Up Project Environment

1. **Create project directory:**
```bash
mkdir fastapi-employee-mgmt
cd fastapi-employee-mgmt
```

2. **Create virtual environment:**
```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

3. **Activate virtual environment:**
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

You should see `(venv)` in your command prompt.

### Step 4: Install Dependencies

Install required packages:
```bash
pip install fastapi uvicorn pymongo python-multipart
```

### Step 5: Set Up MongoDB Atlas

1. Go to [MongoDB Atlas](https://cloud.mongodb.com/)
2. Create a free account
3. Create a new cluster (choose free tier)
4. Create a database user:
   - Go to Database Access
   - Add New Database User
   - Set username/password
5. Whitelist your IP:
   - Go to Network Access
   - Add IP Address (use 0.0.0.0/0 for development)
6. Get connection string:
   - Go to Clusters → Connect
   - Choose "Connect your application"
   - Copy the connection string

### Step 6: Create Your Application

 Use main.py file 

2. **Add your MongoDB connection string:**
   - Replace `MONGO_URI` value with your actual connection string
   - Replace `username`, `password`, and cluster details
   - Example: `"mongodb+srv://myuser:mypass@cluster0.abcde.mongodb.net/?retryWrites=true&w=majority"`

### Step 7: Run the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

You should see output like:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
```

## 🧪 Testing Your API

### Access the Interactive Documentation

Open your web browser and go to:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Sample API Calls

1. **Create an Employee** (POST `/employees`):
```json
{
  "employee_id": "EMP001",
  "name": "John Doe",
  "department": "Engineering",
  "salary": 75000,
  "joining_date": "2024-01-15",
  "skills": ["Python", "FastAPI", "MongoDB"]
}
```

2. **Get All Employees** (GET `/employees`)
3. **Search by Skill** (GET `/employees/search/by-skill?skill=Python`)
4. **Get Average Salary** (GET `/employees/analytics/avg-salary`)


## 🔧 Troubleshooting

### Common Issues:

1. **ModuleNotFoundError**: Make sure virtual environment is activated and dependencies are installed
2. **MongoDB Connection Error**: Check your connection string and network access settings
3. **Port 8000 already in use**: Use `uvicorn main:app --reload --port 8001`

### Environment Variables (Optional):



## 🚀 Next Steps

- Add authentication and authorization
- Implement data validation and error handling
- Add unit tests
- Deploy to cloud platforms (Heroku, AWS, etc.)
- Add logging and monitoring

## 📝 API Endpoints Summary

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint |
| POST | `/employees` | Create new employee |
| GET | `/employees` | Get all employees or filter by department |
| GET | `/employees/{employee_id}` | Get employee by ID |
| PUT | `/employees/{employee_id}` | Update employee |
| DELETE | `/employees/{employee_id}` | Delete employee |
| GET | `/employees/analytics/avg-salary` | Get average salary by department |
| GET | `/employees/search/by-skill` | Search employees by skill |

