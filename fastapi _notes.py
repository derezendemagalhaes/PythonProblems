### Installations
## pip install fastapi
## pip install uvicorn

from fastapi import FastAPI, Path, HTTPException, status # Path is used to validate the data type of the parameter
from pydantic import BaseModel, Field # Field is used to validate the data type of the parameter
# Create/Initialize the app object
app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., example="Milk") # ... means that the field is required
    price: float = Field(..., example=3.99)
    brand: str = Field(..., example="Organic Valley")

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

# Define the root endpoint
@app.get("/")
def home():
    return {"Data": "Test Data"} # This is a dictionary returned as JSON

## PS C:\Users\laris\Documents\project> uvicorn fastapi_test:app --reload
## http://127.0.0.1:8000 open in browser and see {"Data": "Test Data"}
## if we access http://127.0.0.1:8000/docs we can see the documentation of the API

## Create a new endpoint
@app.get("/about")
def about():
    return {"Data": "About Data"}

# inventory = {
#     1: {
#         "name": "Milk",
#         "price": 3.99,
#         "brand": "Organic Valley"
#     },
#     2: {
#         "name": "Eggs",
#         "price": 2.99,
#         "brand": "Organic Valley"
#     }
# }

@app.get("/get-item/{item_id}/{name}")
def get_item(item_id: int, name:str): #you can have multiple parameters
    return inventory[item_id]
     
## How to set a path paramenter
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item you would like to view", gt=0, lt=3)):
    return inventory[item_id]

## How to set a query parameter, comes after the ? in the url
@app.get("/get-by-name")
def get_item(*, name: Optional[str] = None, test: int): # * means that all the parameter are required
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item name not found")

## How to set a query parameter with a path parameter
@app.get("/get-by-name/{item_id}")
def get_item(name: str = Query(None, title="Name", description="Name of the item", min_length=3, max_length=50), item_id: int = Path(None, gt=0, lt=3)):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item name not found")

## Request Body TO SEND INFORMATION TO THE SERVER/Database
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID already exists")
    
    inventory[item_id] = item #{"name": item.name, "price": item.price, "brand": item.brand}
    return inventory[item_id]

## Update and Item
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID does not exist")
    
    inventory[item_id].name = item.name
    inventory[item_id].price = item.price
    inventory[item_id].brand = item.brand
    return inventory[item_id]

## Delete an Item
@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of the item to delete")):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID not found")
    
    del inventory[item_id]
    return {"Success": "Item deleted"}
