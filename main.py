from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define allowed origins (adjust to match your frontend's domain or allow all)
origins = [
    "http://localhost",
    "http://127.0.0.1:9090",
    "http://localhost:9090",           # Frontend local development
    "http://127.0.0.1:5500",       # Frontend local development (if served by Live Server)
    "http://127.0.0.1:8000",
    "http://localhost:8080"

    # You can add your production URL here, e.g., "https://yourdomain.com"
]

# Add CORS middleware to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Origins allowed to access your API
    allow_credentials=True,
    allow_methods=["*"],             # Allow all HTTP methods
    allow_headers=["*"],             # Allow all headers
)

# Mount the static directory where files will be saved
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ensure the static folder exists
Path("static").mkdir(parents=True, exist_ok=True)

# Request body model
class DecodeBase64Request(BaseModel):
    base64_string: str
    output_file_name: str

@app.post("/decode-base64/")
async def decode_base64_file(request: DecodeBase64Request):
    base64_string = request.base64_string
    output_file_name = request.output_file_name

    # Add padding if necessary
    missing_padding = len(base64_string) % 4
    if missing_padding:
        base64_string += '=' * (4 - missing_padding)

    try:
        # Decode the base64 string
        decoded_data = base64.b64decode(base64_string)

        # Save to file in the 'static' directory
        output_path = Path(f"static/{output_file_name}")
        with output_path.open("wb") as output_file:
            output_file.write(decoded_data)

        return {"message": f"File '{output_file_name}' created successfully."}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error decoding base64: {e}")
