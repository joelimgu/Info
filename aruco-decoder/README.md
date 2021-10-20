# Aruco Decoder

Decode an aruco code from an image

## Getting Started

### Installation

Clone the repository

```commandline
git clone https://github.com/ClubRobotInsat/Info
```

Create a virtual environment and activate it
```
cd aruco-decoder
python -m venv venv
venv/script/activate
```

Install the dependencies
```commandline
pip3 install -r requirements.txt
```

## Project Directories

- [`datasets`](datasets): Stores images for processing and testing
- [`aruco`](aruco): library
- [`tests`](tests): A bunch of unitary tests

## Usage

### From an image

```python
from aruco import ArucoDetector

ar = ArucoDetector()
img = "your-image-path"

print(ar.read_image(img))
```
Check [image.py](./examples/image.py)

### From the webcam

Check [camera.py](./examples/camera.py)

## Unittest

Go to [aruco-decoder](../aruco-decoder) and run the following command

```commandline
python -m unittest discover -s ./tests
```
