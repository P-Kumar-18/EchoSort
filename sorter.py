from PIL import Image
import piexif
import os
import shutil


def get_date_time(filePath):
    try:
        img = Image.open(filePath)
        exif_data = piexif.load(img.info["exif"])
        date_time = exif_data["Exif"][piexif.ExifIFD.DateTimeOriginal].decode()
        return date_time
    except Exception as e:
        print(f"Error reading {filePath}: {e}")
        return None
    

def date_and_time(date_time):
    date, time = date_time.replace(":", "-").split(" ")
    return date, time


def EchoSort(date, filePath, fileName):
    target_folder = os.path.join("sorted", date)
    os.makedirs(target_folder, exist_ok = True)
    destination = os.path.join(target_folder, fileName)
    shutil.move(filePath, destination)


def get_photos(photo_folder):
    valid_ext = (".jpg", ".jpeg", ".png")
    photos_list = []
    for file in os.listdir(photo_folder):
        if file.lower().endswith(valid_ext):
            file_path = os.path.join(photo_folder, file)
            photos_list.append((file, file_path))
    return photos_list