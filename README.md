# Morphology Image Processing Tool

A desktop application for performing morphological image processing operations such as Dilate, Erode, Open, Close, Gradient, Top Hat, Black Hat, and custom combinations.

## Author
**Diego André Sant'Ana** - diego.santana@ifms.edu.br

## Version
1.0.0

## Description
This tool provides a graphical interface to apply various morphological transformations to images. It's useful for image preprocessing, noise removal, edge detection, and feature extraction in computer vision applications.

### Features
- **Load Images**: Support for JPG and PNG formats
- **Adjustable Kernel Size**: Customize the morphological kernel size (1-100)
- **Multiple Operations**:
  - Grayscale conversion
  - Erode
  - Dilate
  - Open
  - Close
  - Morphological Gradient
  - Top Hat
  - Black Hat
  - Custom: Dilate + Open + Erode
- **Real-time Preview**: View all transformations simultaneously
- **Interactive GUI**: User-friendly interface with side-by-side comparison

## Requirements

### Python Version
- Python 2.7 or Python 3.x

### Dependencies
Install the required packages using pip:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install numpy opencv-python pillow
```

**Note**: Tkinter comes pre-installed with Python on most systems. If you're on Linux, you may need to install it separately:
```bash
sudo apt-get install python-tk  # For Python 2
sudo apt-get install python3-tk  # For Python 3
```

## Installation

### Python Version

1. Clone this repository:
```bash
git clone <repository-url>
cd morphology
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python pyMorphology.py
```

### JavaScript/Electron Version

1. Navigate to the jsMorphology directory:
```bash
cd jsMorphology
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Run the application:
```bash
npm start
```

**Note**: You need Node.js and npm installed. Download from [nodejs.org](https://nodejs.org/)

## How to Use

1. Launch the application using the command above
2. Click **"Select Image"** to load a JPG or PNG image
3. Adjust the **Kernel size** using the spinbox (default: 1)
4. Click **"Run Process"** to apply all morphological operations
5. View the results in the grid of transformed images

## 🌐 Try Online (No Installation Required)

A fully functional browser version is available via **GitHub Pages**! Just access the link below to use the tool directly in your browser - no installation, no setup.

🔗 **Access**: `https://yourusername.github.io/your-repo-name/`

**Features:**
- ✅ Runs 100% in the browser using OpenCV.js
- ✅ Works on any device (Windows, Mac, Linux, tablets, phones)
- ✅ All morphological operations available
- ✅ Adjustable kernel size with real-time preview
- ✨ Created with **QWEN AI**

---

## Directory Structure

```
morphology/
├── pyMorphology.py      # Main application (Python version)
├── jsMorphology/        # JavaScript/Electron version
│   ├── main.js          # Electron main process
│   ├── renderer.js      # Browser-side logic
│   ├── index.html       # UI template
│   ├── styles.css       # Styling
│   └── package.json     # Node.js dependencies
├── docs/                # Browser-only version for GitHub Pages
│   ├── index.html       # Complete browser version with OpenCV.js
│   └── GITHUB_PAGES_GUIDE.md  # Deployment instructions
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Technologies Used

### Python Version
- **Tkinter**: GUI framework
- **OpenCV (cv2)**: Image processing operations
- **PIL/Pillow**: Image handling and display
- **NumPy**: Array operations

### JavaScript Version
- **Electron**: Desktop application framework
- **OpenCV.js**: Image processing in the browser
- **HTML/CSS/JavaScript**: Frontend interface

### Browser Version (GitHub Pages)
- **OpenCV.js**: Pure browser-based image processing
- **Vanilla JavaScript**: No frameworks needed
- **Modern HTML5/CSS3**: Responsive design

## License
This project is open source and available for educational purposes.

## Acknowledgments
- Discipline: Computer Vision
- Date: 05/09/2018  

## Credits
Created with the assistance of **QWEN AI**.


