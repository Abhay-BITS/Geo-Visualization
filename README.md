# Cesium Head Tracking with Depth Data using Intel Realsense Sensor

This project involves integrating head orientation data from a WebSocket into a CesiumJS application for visualizing a 3D object, specifically Mount Fuji. The project also utilizes Intel RealSense camera for enhanced visualization with depth data.


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Dependencies](#dependencies)
- [License](#license)

## Introduction
This project leverages CesiumJS for 3D visualization and MediaPipe for head tracking. It demonstrates how to use head orientation data to manipulate the view of a 3D object in a CesiumJS scene. Additionally, the project uses the Intel RealSense camera to provide depth data for better visualization.


## Features
- Real-time head tracking using MediaPipe FaceMesh.
- Integration with CesiumJS for 3D visualization.
- Real-time data updates via WebSocket.
- Enhanced visualization with depth data using Intel RealSense camera.

## Installation
1. Clone the repository:
   ```sh
   git clone <repository-url>
   
2. Navigate to the project directory:
   ```sh
   cd <project-directory>

## Usage
- Connect the Intel RealSense camera to your computer.
- Open index.html in a web browser to start the application.
- Ensure your webcam is connected and accessible.
- The Cesium viewer will display the 3D visualization of Mount Fuji, with the view controlled by your head movements and enhanced by depth data from the Intel RealSense camera.

## Files 
- 'VideoGetHD.py': Script for video handling and processing.
- 'VideoGetHD.cpython-312.pyc': Compiled Python bytecode file for VideoGetHD.py.
- 'FaceTracker.py': Script for tracking facial landmarks using MediaPipe.
- 'VirtualWindow.py': Script for creating a virtual window for visualization.
- 'index.html': Main HTML file for the project.
- 'script.js': JavaScript file that initializes the Cesium viewer and handles head tracking.

## Dependencies

- **CesiumJS:** A JavaScript library for 3D globes and maps.
  - [CesiumJS Documentation](https://cesium.com/docs/)
  - To include CesiumJS in your project, add the following to your `index.html`:
    ```html
    <script src="https://cesium.com/downloads/cesiumjs/releases/1.78/Build/Cesium/Cesium.js"></script>
    <link href="https://cesium.com/downloads/cesiumjs/releases/1.78/Build/Cesium/Widgets/widgets.css" rel="stylesheet">
    ```

- **MediaPipe FaceMesh:** A library for face detection and tracking.
  - [MediaPipe FaceMesh Documentation](https://google.github.io/mediapipe/solutions/face_mesh.html)
  - To install MediaPipe FaceMesh, use the following command:
    ```sh
    pip install mediapipe
    ```

- **Python:** Required for running the `.py` scripts.
  - [Python Documentation](https://www.python.org/doc/)
  - Ensure Python is installed on your system. Download it from [python.org](https://www.python.org/downloads/).

- **Intel RealSense SDK:** Required for utilizing the RealSense camera for depth data.
  - [Intel RealSense SDK Documentation](https://dev.intelrealsense.com/docs/sdk-2)
  - To install the Intel RealSense SDK, follow the instructions provided in the [installation guide](https://github.com/IntelRealSense/librealsense/blob/master/doc/installation.md).

- **pyrealsense2:** Python wrapper for Intel RealSense SDK.
 items.
  - [pyrealsense2 Documentation](https://pypi.org/project/pyrealsense2/)
  - To install pyrealsense2, use the following command:
    ```sh
    pip install pyrealsense2
    ```

## License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

   
