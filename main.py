from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define the root endpoint
@app.get("/")
def read_root():
    """
    This endpoint returns a simple "Hello, World!" message.
    It's a great way to verify that the API is running.
    """
    return {"message": "Hello, World!"}

@app.get("/health")
def health_check():
    """
    This endpoint is used for health checks.
    It returns a simple status message to show the API is healthy.
    """
    return {"status": "ok"}
