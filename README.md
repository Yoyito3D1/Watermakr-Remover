# 🖼️ PDF Watermark Remover & Image Processor 🖼️

Welcome to this project! 🚀  
This Python tool allows you to remove light-colored watermarks from PDFs by converting them into images, processing the pixels, and reconstructing a clean PDF. Perfect for cleaning up scanned documents or preparing PDFs for further use. ✨

---

## 🎯 Project Overview
This project provides a workflow to clean PDFs efficiently:

1. **Convert PDF pages into images** – Each page of the PDF is converted into an image for pixel-level processing.
2. **Process images to remove watermarks** – Light-colored pixels, which often correspond to watermarks or pale backgrounds, are replaced with white. This creates a visually clean version of each page.
3. **Reassemble the cleaned images into a final PDF** – After processing, the images are combined back into a single PDF that mirrors the original document but without unwanted watermarks.

The tool is designed to handle multiple pages, maintain their order, and provide both individual processed images and a final merged PDF.

---

## 🛠️ Features & Benefits
- ✅ Removes light-colored watermarks efficiently.
- ✅ Works with any PDF file.
- ✅ Maintains original page order automatically.
- ✅ Outputs both individual images and a final clean PDF.
- ✅ Uses widely available Python libraries: `pdf2image`, `scikit-image`, `Pillow`, `NumPy`.

---

## 📈 Usage Workflow
1. Place your PDF in the project folder (e.g., `marca_aigua.pdf`).
2. Run the Python script to start the conversion and processing pipeline.
3. Processed images are saved in a dedicated folder with numbered filenames to preserve page order.
4. All processed images are merged into a single PDF for final output.
5. Optionally, you can preview each page individually via the saved images.

---

## 🛠️ Requirements
Make sure you have Python 3.x and the following packages installed:

- `pdf2image`
- `scikit-image`
- `Pillow`
- `NumPy`

Additionally, **Poppler** must be installed for `pdf2image` to work correctly.

---

## 📊 Benefits & Insights
- The tool allows for automated PDF cleanup without manual image editing.
- Preserves document structure while removing unwanted visual artifacts.
- Easy to extend for different color thresholds or watermark patterns.
- Helps prepare scanned documents for professional presentation or archival.

---

## 🙌 Contributions & Credits
- Developed as a practical Python project for PDF processing and watermark removal.
- Utilizes open-source libraries for image conversion and processing.
- Inspired by the need for clean, professional PDF documents.

---

## 📫 Contact & Support
If you want to discuss improvements, report bugs, or contribute, feel free to open an issue or reach out! ✉️  

Thank you for checking out this project! 🚀  
Clean PDFs quickly and efficiently with Python! 🖼️💡
