import datetime
import os
import shutil


def get_date_time(filePath):
    try:
        date_time = os.path.getmtime(filePath)
        date_time = datetime.datetime.fromtimestamp(date_time)
        return date_time.strftime("%d-%m-%Y %H-%M-%S")
    except Exception as e:
        print(f"Error reading {filePath}: {e}")
        return None


def date_and_time(date_time):
    date, time = date_time.split(" ")
    return date, time


def EchoSort(date, filePath, fileName, log_file, output_base):
    try:
        target_folder = os.path.join(output_base, "sorted", date)
        os.makedirs(target_folder, exist_ok=True)
        destination = os.path.join(target_folder, fileName)
        shutil.move(filePath, destination)
        log_file.write(f"Moved: {filePath} -> {destination}\n")
    except Exception as e:
        log_file.write(f"Error: {filePath} -> {e}\n")


def get_photos(photo_folder):
    valid_ext = (".jpg", ".jpeg", ".png")
    photos_list = []
    for file in os.listdir(photo_folder):
        if file.lower().endswith(valid_ext):
            file_path = os.path.join(photo_folder, file)
            photos_list.append((file, file_path))
    return photos_list