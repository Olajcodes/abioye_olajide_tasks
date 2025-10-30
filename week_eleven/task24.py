# Importing necessary libraries
from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from typing import Optional
import uvicorn
import os

load_dotenv()

# Creating an instance 
app = FastAPI(title="Simple FASTAPI App", version="1.0.0")


# Creating a list of dictionary in place of database
data = [
    {"name": "Abioye Olajide", "track": "Fullstack Developer", "age": 25 },
    {"name": "Abioye Abdullateef", "track": "AI Developer", "age": 29},
    {"name": "Olajide Abdullateef", "track": "AI Engineer", "age": 35},
]

# Creating a class for the API
class Item(BaseModel):
    name: str = Field(..., examples=["John Doe"])
    track: str = Field(..., examples=["Data Analyst"])
    age: int = Field(..., examples=[20])
    
# Creating an optional class for updating details
class update_item(BaseModel):
    name: Optional[str] = None
    track: Optional[str] = None
    age: Optional[int] = None
    
# Implementing the update(PATCH) function
@app.patch("/patch-data/{id}")
def patch_data(id: int, req: update_item):
    if id >= len(data):
        return {"Error": "Index out of range."}
    data[id].update(req.model_dump(exclude_unset=True))
    print(data)
    return {"Message": "Data Edited", "Data": data}


# Implementing the delete(REMOVE) function
@app.delete("/delete-data/{id}")
def delete_data(id: int):
    if id >= len(data):
        return {"Error": "Index Error"}
    data.pop(id)
    print(data)
    return {"Message": "Data Deleted", "Data": data}


if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port"))) # type: ignore