# Object Recognition in Photos

## Description
This is an open-source project designed to help users identify objects in a photo. The project is developed using FastAPI, a robust and efficient framework for building APIs. It leverages libraries such as torch and torchvision for training models, along with JavaScript, HTML, and SCSS for UI development. The main objective of the project is to facilitate rapid scene recognition through a camera to assist visually impaired individuals. This project marks just the initial phase of development.

## Setup Instructions

### 1. Clone Repository from GitHub
```sh
git clone https://github.com/LemonFT/DescribeTheObjectInThePhoto.git
```
### 2.Set up backend

#### Go to directory backend
```
cd deeplearningg
```
#### Simulate the VENV virtual machine environment
```
python -m venv venv
venv\Scripts\activate [Windows]
source venv/bin/activate [Linux/Mac]
```
#### Install dependencies
```
pip install -r requirements.txt
```
#### Run backend
```
uvicorn api:app --reload
```
### 3.Set up frontend
#### Go to directory frontend
```
cd uxui
```
#### Install live server
```
npm install -g live-server
```
#### Start server
```
live-server --port=3000
```
## Use
After successfully launching the project, you can upload images and check the program's description results for those images.
## Contact 
If you have any questions or feedback about this project, feel free to reach out to us:
Email: lemonftdev@gmail.com
We welcome your input and look forward to hearing from you!

