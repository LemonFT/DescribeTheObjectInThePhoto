import asyncio
import io
from io import BytesIO
from typing import List

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from PIL import Image
from torchvision import transforms

from models.image_re import image_recognition

# from models.run import testmodel

app = FastAPI()
origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 
# @app.get("/")
# async def root():
#     return {"mess": "api root"};

@app.post("/upload")
async def upload_image(file: UploadFile = UploadFile(...)):
    
    print(file)
    # Đảm bảo file có định dạng hợp lệ (ví dụ: image/jpeg, image/png)
    if file.content_type not in ["image/jpeg", "image/png"]:
        return JSONResponse(status_code=415, content={"message": "Unsupported Media Type"})

    # Đọc dữ liệu nhị phân của file
    file_contents = await file.read()
    result = await image_recognition(io.BytesIO(file_contents))
    return JSONResponse(status_code=200, content={"content": result})
