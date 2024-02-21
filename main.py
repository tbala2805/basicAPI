# importing the function 
from add import addition 

# let's import fastAPI from fastapi package
from fastapi import FastAPI 

# creating an app instance 
app = FastAPI()

# using get method with app
# home page 
@app.get('/')
def home():
    return {
        "message" : "we are in home page"
    }

# for calling addtion function 
@app.get('/add')
def adding(): 
    return {
        "message": "we are in add page",
        "addition ": addition()

    }

# Run the FastAPI app with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=80)