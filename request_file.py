from typing import Annotated
import shutil
from pathlib import Path
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def main():
    content = """
<body>
<form action="/uploadfile/" enctype="multipart/form-data" method="post">
<input name="file" type="file">
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    upload_dir = Path("uploads")
    file_path = upload_dir / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"info": f"file '{file.filename}' saved at '{file_path}'"}


@app.get("/multiple")
async def main():
    content = """
<body>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    saved_files = []
    upload_dir = Path("uploads")
    
    for file in files:
        try:
            # Create secure file path (prevent directory traversal)
            file_path = upload_dir / file.filename
            
            # Save the file
            with file_path.open("wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            saved_files.append({
                "filename": file.filename,
                "saved_path": str(file_path),
                "size": file_path.stat().st_size
            })
            
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error saving file {file.filename}: {str(e)}"
            )
        finally:
            await file.close()
    
    return {"saved_files": saved_files, "total_files": len(saved_files)}