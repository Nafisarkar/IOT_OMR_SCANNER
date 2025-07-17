<div align="center">

# 🔍 IoT OMR Scanner

**Automated Optical Mark Recognition System with ESP32-CAM**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![ESP32](https://img.shields.io/badge/ESP32-CAM-red.svg)](https://www.espressif.com/)

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Hardware](#-hardware-requirements) • [Contributing](#-contributing)

</div>

---

## 📖 About

The **IoT OMR Scanner** is an innovative IoT-based solution that automates the evaluation of OMR (Optical Mark Recognition) sheets. Combining the power of ESP32-CAM for image capture with advanced OpenCV algorithms, this system provides accurate, real-time processing for educational institutions and examination centers.

## ✨ Features

### 📷 Smart Image Capture

- **High-resolution imaging** with ESP32-CAM module
- **Cost-effective** and compact hardware solution
- **Wireless connectivity** for remote operation

### 🧠 Advanced Computer Vision

- **Intelligent preprocessing** with grayscale conversion and Gaussian blur
- **Precise edge detection** using Canny Edge Detector
- **Accurate circle detection** via Hough Circle Transform

### ✅ Automated Answer Validation

- **Smart positioning** algorithm (top-to-bottom, left-to-right sorting)
- **Real-time comparison** with predefined answer keys
- **Visual feedback** with color-coded results:
  - 🔴 **Red circles**: Correct answers
  - 🟢 **Green circles**: Incorrect answers

### ⚡ Real-Time Processing

- **Fast evaluation** suitable for high-volume environments
- **Instant results** with detailed analytics
- **Educational-grade accuracy** for reliable assessments

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- ESP32-CAM module with firmware

### Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/Nafisarkar/IOT_OMR_SCANNER.git
   cd IOT_OMR_SCANNER
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:

   ```bash
   pip install opencv-python numpy imutils
   ```

3. **Configure ESP32-CAM**

   - Flash the ESP32-CAM with the provided firmware
   - Set up wireless connection parameters

4. **Setup paths**
   - Update image paths in the configuration file
   - Ensure proper directory structure

## 📱 Usage

### Step-by-Step Process

1. **📸 Capture Image**

   ```
   Use ESP32-CAM to capture OMR sheet → Save to img/ folder
   ```

2. **🔧 Run Scanner**

   ```bash
   python main.py
   ```

3. **📊 View Results**
   - Processed image with highlighted answers
   - Console output with detection statistics
   - Accuracy metrics and analysis

### Expected Output

```
Total circles detected: 40
Correct answers: 35
Accuracy: 87.5%
```

### Core Components

| Component               | Technology       | Purpose                               |
| ----------------------- | ---------------- | ------------------------------------- |
| **Image Preprocessing** | OpenCV           | Noise reduction, grayscale conversion |
| **Edge Detection**      | Canny Algorithm  | Boundary identification               |
| **Circle Detection**    | Hough Transform  | Mark recognition                      |
| **Validation Engine**   | Custom Algorithm | Answer comparison                     |

## 📋 Hardware Requirements

### Essential Components

- 🔧 **ESP32-CAM Module**
- 🔧 **ESP32 Development Board**
- 🔌 **Power Supply** (USB Cable or external)
- 📄 **OMR Sheets** (standard format)

### Optional Enhancements

- 💡 **LED Lighting** for better image quality
- 📦 **Enclosure** for portable operation
- 🔋 **Battery Pack** for mobile use

## 💻 Software Stack

| Technology  | Version | Purpose              |
| ----------- | ------- | -------------------- |
| **Python**  | 3.7+    | Core processing      |
| **OpenCV**  | 4.x     | Computer vision      |
| **NumPy**   | Latest  | Numerical operations |
| **Imutils** | Latest  | Image utilities      |

## 🎯 Example Results

### Before Processing

![Input OMR Sheet](img/image.png)

### After Processing

- ✅ **Correct answers**: Highlighted in red
- ❌ **Incorrect answers**: Highlighted in green
- 📊 **Statistics**: Displayed in terminal

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🍴 Fork** the repository
2. **🌟 Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **💾 Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **📤 Push** to the branch (`git push origin feature/AmazingFeature`)
5. **🔀 Open** a Pull Request

### Areas for Contribution

- 🐛 Bug fixes and improvements
- 📚 Documentation enhancements
- ✨ New features and algorithms
- 🧪 Test coverage expansion

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenCV Community** - For providing powerful computer vision tools
- **ESP32 Community** - For comprehensive documentation and support
- **Contributors** - For making this project better

## 📬 Contact & Support

- **Author**: Shaon An Nafi
- **Issues**: [GitHub Issues](https://github.com/Nafisarkar/IOT_OMR_SCANNER/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Nafisarkar/IOT_OMR_SCANNER/discussions)

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

[🔝 Back to top](#-iot-omr-scanner)

</div>
