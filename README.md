# 📸 EchoSort

**EchoSort** is a minimalistic yet powerful photo-sorting and organizing tool that helps bring order to your digital photo library by automatically sorting images into date-based folders — using their **last modified timestamp**.

Whether you're organizing a messy phone backup or cleaning up thousands of camera shots, **EchoSort** does the heavy lifting with just a click.

---

## 🚀 Features

- 📁 **Auto-sorts photos** into folders like: `sorted/15-06-2025/`
- 🕒 Uses **file modified date** as a reliable timestamp
- 🖼️ Supports `.jpg`, `.jpeg`, and `.png` files
- 🧹 Skips unreadable or unsupported files gracefully
- 🪟 Clean **Tkinter GUI** for folder selection
- 🧾 Generates a `log.txt` summarizing all operations
- 🧠 Modular code with a clean separation of logic and UI
- 🔒 Safe paths using `os.path.join` for cross-platform compatibility
- 📦 Ready to package as `.exe` with PyInstaller (custom icon supported)

---

## 🛠️ Requirements

- Python 3.x  
- [Pillow](https://pypi.org/project/Pillow/) *(for image handling)*  
- [piexif](https://pypi.org/project/piexif/) *(optional, if you later add EXIF reading)*

### ✅ Install dependencies

```bash
pip install pillow piexif