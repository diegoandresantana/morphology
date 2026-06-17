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

## 🌐 Browser Version (GitHub Pages)

**Want to try without installing anything?** We have a browser-only version that runs 100% in your browser!

### Quick Start - Enable GitHub Pages:

1. Go to your repository **Settings** → **Pages**
2. Under **Source**, select **Deploy from a branch**
3. Choose branch: **main** (or **master**)
4. Choose folder: **/docs (root)**
5. Click **Save**
6. Wait ~1-2 minutes for deployment
7. Access at: `https://yourusername.github.io/your-repo-name/`

### Features:
- ✅ **No installation required** - runs directly in the browser
- ✅ **Works on any device** - Windows, Mac, Linux, tablets, phones
- ✅ **All morphological operations** - same as desktop versions
- ✅ **Adjustable kernel size** - real-time slider control
- ✅ **Instant processing** - powered by OpenCV.js
- ✅ **Free hosting** - GitHub Pages is completely free
- ✨ **Created with QWEN AI**

### Files Included:
- `docs/index.html` - Complete browser application with OpenCV.js via CDN
- `docs/GITHUB_PAGES_GUIDE.md` - Detailed deployment instructions and alternatives

### How It Works:
The browser version uses **OpenCV.js** loaded directly from the official OpenCV CDN, so there are no dependencies to install. Everything runs client-side in the user's browser using WebAssembly for near-native performance!

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
- ✨ Created with QWEN AI

## License
This project is open source and available for educational purposes.

## Acknowledgments
- Discipline: Computer Vision
- Date: 05/09/2018  

## Credits
The JavaScript/Electron version was created with the assistance of **QWEN** AI.

The browser-only version (GitHub Pages) was also created with **QWEN** AI, making it easy to share and access the tool without any installation! 🎉


