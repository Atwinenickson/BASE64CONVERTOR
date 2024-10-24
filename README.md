# Base64 to File Converter

This project allows you to convert Base64 strings into downloadable files via a FastAPI backend and a simple frontend interface.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)
- Tailwind CSS for frontend styling (using CDN)
- Alpine.js for frontend logic (using CDN)

## Backend Setup (FastAPI)

The backend provides an API to decode Base64 strings and save the output as a file.

### Prerequisites

Before running the backend, ensure you have Python 3.7+ installed.

### Install the required Python dependencies:

1. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

2. Install FastAPI and Uvicorn:

    ```bash
    pip install fastapi uvicorn
    ```

### Running the Backend

1. Place the `main.py` file in your project directory (e.g., `/backend/main.py`).
2. Start the FastAPI backend using Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

3. The backend server should now be running on `http://127.0.0.1:8000`.

4. The API endpoint for decoding Base64 and downloading files is available at:

    - `POST http://127.0.0.1:8000/decode-base64/`

### Backend Directory Structure

backend/ │ ├── main.py # FastAPI backend logic └── static/ # Folder where decoded files will be saved



## Frontend Setup (HTML/JavaScript)

The frontend provides an interface for users to input Base64 strings, specify a file name, and download the resulting file.

### Running the Frontend

1. Place the `main.html` file in a directory (e.g., `/frontend/main.html`).
2. Open the `main.html` file in your browser (you can simply double-click it or serve it using a local server).

### Option 1: Using Live Server (Recommended)

You can use a simple web server to serve the HTML file. This is helpful for testing CORS requests.

1. You can install a simple live server such as [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) in VSCode or any other development server.

2. Once installed, right-click `main.html` and select "Open with Live Server". This will start the frontend on a different port (e.g., `http://127.0.0.1:5500`).

### Option 2: Direct File Access

Simply open `main.html` in your browser, but note that CORS policies might restrict direct access to the backend in some browsers.

### Frontend Directory Structure

frontend/ │ └── main.html # HTML page with Base64 converter interface



### Frontend Features

- **Input Base64 String**: Allows users to input the Base64-encoded string.
- **Input File Name**: Specify the name of the file to be downloaded (e.g., `file.pdf`).
- **Download Button**: Downloads the file once it has been created on the backend.
- **View PDF Button**: Opens the downloaded file in a new tab for viewing.

## Notes

- Ensure both backend and frontend are running on the same machine.
- CORS has been configured to allow requests from the frontend to the backend.
- If needed, modify the allowed origins in the FastAPI backend's CORS configuration to match your environment.

## Example Usage

1. Start the backend server:

    ```bash
    uvicorn main:app --reload
    ```

2. Open the frontend by either serving `main.html` or opening it directly in your browser.

3. Enter the Base64 string, file name, and click the "Download" button. You can then view the generated file by clicking the "View PDF" button.

## License

This project is licensed under the MIT License.
