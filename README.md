# IOT_OMR_SCANNER

The **IOT_OMR_SCANNER** is an IoT-based project designed to automate the evaluation of OMR (Optical Mark Recognition) sheets. By using an ESP32 microcontroller paired with the ESP32-CAM module, this project captures high-resolution images of OMR sheets and processes them using OpenCV to detect and validate answers against a predefined answer key.

---

## Features

1. **Image Capture with ESP32-CAM**
   - High-resolution image capture of OMR sheets.
   - Compact and cost-effective hardware solution.

2. **OpenCV Integration**
   - Grayscale conversion and Gaussian blur for noise reduction.
   - Edge detection using the Canny Edge Detector.
   - Circle detection on OMR sheets using Hough Circle Transform.

3. **Answer Validation**
   - Automatically sorts detected circles based on their position (top-to-bottom, left-to-right).
   - Compares detected answers with a predefined answer key.
   - Highlights correct answers in red and incorrect answers in green on the output image.

4. **Real-Time Processing**
   - Fast and efficient evaluation of OMR sheets, making it suitable for educational institutions and exam evaluations.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/IOT_OMR_SCANNER.git
   ```

2. Install the required Python libraries:
   ```bash
   pip install opencv-python numpy imutils
   ```

3. Flash the ESP32-CAM module with the necessary firmware for image capture.

4. Configure the paths in the script to match your local environment.

---

## Usage

1. **Capture an Image**:
   - Use the ESP32-CAM module to capture an image of the OMR sheet.

2. **Run the Script**:
   - Place the captured image in the specified folder (e.g., `img/`).
   - Execute the Python script:
     ```bash
     python omr_scanner.py
     ```

3. **Output**:
   - The script processes the image and highlights the answers:
     - **Red circles**: Correct answers.
     - **Green circles**: Incorrect answers.
   - Displays the total number of detected circles and matched answers in the terminal.

---

## Code Overview

- **Image Preprocessing**:
  - Grayscale conversion and Gaussian blur to reduce noise.
  - Edge detection using Canny Edge Detector.

- **Circle Detection**:
  - Hough Circle Transform for detecting marked circles.

- **Answer Validation**:
  - Compares the detected circles with a predefined answer key.
  - Highlights answers based on correctness.

- **Visualization**:
  - Outputs a resized and annotated image for easy verification.

---

## Example

### Input Image:
An OMR sheet image captured using the ESP32-CAM module.

### Output Image:
A processed image with:
- Correct answers highlighted in **red**.
- Incorrect answers highlighted in **green**.

---

## Hardware Requirements

1. **ESP32-CAM Module**
2. **ESP32 Development Board**
3. Power Supply or USB Cable
4. OMR Sheets

---

## Software Requirements

1. Python 3.7 or above
2. Required Libraries:
   - OpenCV
   - NumPy
   - Imutils

---

## Contribution

Contributions are welcome! Feel free to submit a pull request or open an issue for bug reports or feature suggestions.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Acknowledgements

- **OpenCV**: For providing powerful computer vision tools.
- **ESP32 Community**: For documentation and support.

---

## Contact

For any inquiries or feedback, feel free to contact me at [your_email@example.com].

