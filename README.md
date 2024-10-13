# Roll-Pitch-Yaw GUI Display

<!-- ABOUT THE PROJECT -->
## About The Project
Roll-Pitch-Yaw GUI Display is a graphical user interface (GUI) application for visualizing and controlling roll, pitch, and yaw angles of a vehicle. The GUI is built using Python, leveraging the `tkinter` and `customtkinter` libraries, with the `Pillow` library for image manipulation. The app provides real-time visualization of pitch and roll through sliders and an interactive display representing the vehicle's orientation.

<img width="299" alt="Ekran Resmi 2023-01-04 14 59 46" src="https://user-images.githubusercontent.com/57351922/210551543-b2db81bd-5ef6-4dfa-a640-39c0bc04e398.png">

### Built With
* [![Python][Python-logo]][Python-url]

<!-- FEATURES -->
## Features
* Python Programming Language: Built using Python 3.11.0
* Roll and Pitch Control: Adjust the roll and pitch values of the vehicle using interactive sliders.
* Image Manipulation: Real-time image rotation to simulate roll and vertical adjustment to simulate pitch.
* Customizable GUI: Built using `customtkinter` for enhanced GUI components.
* Real-Time Updates: Immediate feedback through graphical adjustments based on user input.

<!-- HOW TO BUILD -->
## How to Build
1. Clone the repository:
   ```sh
   git clone https://github.com/altugparlak/Roll-Pitch-Yaw-GUI_Display.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Roll-Pitch-Yaw-GUI_Display
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Make sure the required images (`RPY.png` and `vehicle.png`) are available in the same directory as the script.
5. Run the application:
   ```sh
   python app.py
   ```

<!-- FILE STRUCTURE -->
## File Structure
```sh
.
├── app.py          # Main Python script
├── RPY.png         # Image for roll-pitch display
└── vehicle.png     # Image representing the vehicle
```

<!-- REQUIREMENTS -->
## Requirements
* `tkinter`
* `customtkinter`
* `Pillow`

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python-logo]: https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg
[Python-url]: https://www.python.org/
