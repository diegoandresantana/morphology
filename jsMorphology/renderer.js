const { ipcRenderer } = require('electron');

let originalImage = null;
let cvReady = false;

// Check if OpenCV is ready
function onOpenCvReady() {
    cvReady = true;
    const statusDiv = document.createElement('div');
    statusDiv.id = 'status';
    statusDiv.textContent = 'OpenCV.js Ready!';
    document.body.appendChild(statusDiv);
    statusDiv.style.display = 'block';
    setTimeout(() => {
        statusDiv.style.display = 'none';
    }, 3000);
    console.log('OpenCV.js is ready!');
}

// Select image button handler
document.getElementById('selectImageBtn').addEventListener('click', async () => {
    try {
        const result = await ipcRenderer.invoke('select-image');
        if (result) {
            document.getElementById('imagePath').textContent = result.path;
            
            // Load image into OpenCV
            const imgElement = document.createElement('img');
            imgElement.src = 'data:image/jpeg;base64,' + result.data;
            imgElement.onload = () => {
                originalImage = imgElement;
                
                // Display original image in first panel
                displayImage(imgElement, 'img1');
            };
        }
    } catch (error) {
        console.error('Error selecting image:', error);
    }
});

// Run process button handler
document.getElementById('runProcessBtn').addEventListener('click', () => {
    if (!originalImage || !cvReady) {
        alert('Please select an image and wait for OpenCV to load.');
        return;
    }
    
    const kernelSize = parseInt(document.getElementById('kernelSize').value);
    processImage(originalImage, kernelSize);
});

// Display image in a container
function displayImage(mat, containerId) {
    const container = document.getElementById(containerId);
    container.innerHTML = '';
    
    // Create canvas from OpenCV mat
    const canvas = document.createElement('canvas');
    canvas.width = mat.cols;
    canvas.height = mat.rows;
    const ctx = canvas.getContext('2d');
    
    // Create ImageData from mat
    const imageData = new ImageData(mat.data, mat.cols, mat.rows);
    
    // Put image data on canvas
    const tempCanvas = document.createElement('canvas');
    tempCanvas.width = mat.cols;
    tempCanvas.height = mat.rows;
    const tempCtx = tempCanvas.getContext('2d');
    tempCtx.putImageData(imageData, 0, 0);
    
    // Draw to main canvas
    ctx.drawImage(tempCanvas, 0, 0);
    
    // Create img element
    const img = document.createElement('img');
    img.src = canvas.toDataURL();
    img.alt = containerId;
    
    container.appendChild(img);
}

// Process image with all morphology operations
function processImage(imgElement, kernelSize) {
    try {
        // Read image
        let src = cv.imread(imgElement);
        let dst = new cv.Mat();
        
        // Convert to grayscale
        cv.cvtColor(src, src, cv.COLOR_RGBA2GRAY, 0);
        
        // Display original grayscale
        displayImage(src, 'img1');
        
        // Create kernel
        let M = cv.Mat.ones(kernelSize, kernelSize, cv.CV_8U);
        let anchor = new cv.Point(-1, -1);
        
        // Erode
        cv.erode(src, dst, M, anchor, 1, cv.BORDER_CONSTANT, cv.morphologyDefaultBorderValue());
        displayImage(dst, 'img2');
        
        // Dilate
        cv.dilate(src, dst, M, anchor, 1, cv.BORDER_CONSTANT, cv.morphologyDefaultBorderValue());
        displayImage(dst, 'img3');
        
        // Open
        cv.morphologyEx(src, dst, cv.MORPH_OPEN, M, anchor, 1, cv.BORDER_CONSTANT, cv.morphologyDefaultBorderValue());
        displayImage(dst, 'img4');
        
        // Close
        cv.morphologyEx(src, dst, cv.MORPH_CLOSE, M, anchor, 1, cv.BORDER_CONSTANT, cv.morphologyDefaultBorderValue());
        displayImage(dst, 'img5');
        
        // Morphological Gradient
        cv.morphologyEx(src, dst, cv.MORPH_GRADIENT, M, anchor, 1, cv.BORDER_CONSTANT, cv.morphologyDefaultBorderValue());
        displayImage(dst, 'img6');
        
        // Top Hat
        cv.morphologyEx(src, dst, cv.MORPH_TOPHAT, M, anchor, 1, cv.BORDER_CONSTANT, cv.morphologyDefaultBorderValue());
        displayImage(dst, 'img7');
        
        // Black Hat
        cv.morphologyEx(src, dst, cv.MORPH_BLACKHAT, M, anchor, 1, cv.BORDER_CONSTANT, cv.morphologyDefaultBorderValue());
        displayImage(dst, 'img8');
        
        // Dilate + Open + Erode
        cv.dilate(src, dst, M, anchor, 1, cv.BORDER_CONSTANT, cv.morphologyDefaultBorderValue());
        cv.morphologyEx(dst, dst, cv.MORPH_OPEN, M, anchor, 1, cv.BORDER_CONSTANT, cv.morphologyDefaultBorderValue());
        cv.erode(dst, dst, M, anchor, 1, cv.BORDER_CONSTANT, cv.morphologyDefaultBorderValue());
        displayImage(dst, 'img9');
        
        // Clean up
        src.delete();
        dst.delete();
        M.delete();
        
    } catch (error) {
        console.error('Error processing image:', error);
        alert('Error processing image. Check console for details.');
    }
}

// Handle window resize
window.addEventListener('resize', () => {
    // Optional: Add responsive behavior
});

console.log('Renderer process started');
