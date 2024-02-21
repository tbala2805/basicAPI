from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()

# Define a route
@app.get("/")
async def read_root():
    return {"message": "Hello, World"}

# Run the FastAPI app with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=90)
