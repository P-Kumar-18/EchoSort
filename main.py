from sorter import get_date_time, date_and_time, get_photos, EchoSort
from gui import app
from utility import get_exe_path
import os


def main():
    photos_folder = app()
    if photos_folder:
        photos = get_photos(photos_folder)
        moved = 0
        skipped = 0
        failed = 0

        log_path = os.path.join(get_exe_path(), "log.txt")
        with open(log_path, "w", encoding="utf-8") as log_file:
            for fileName, filePath in photos:
                date_time = get_date_time(filePath)
                if date_time:
                    try:
                        date, time = date_and_time(date_time)
                        EchoSort(date, filePath, fileName, log_file, photos_folder)
                        moved += 1
                    except Exception as e:
                        log_file.write(f"Error parsing data for {filePath}: {e}\n")
                        failed += 1
                else:
                    log_file.write(f"Skipped: no modified time for {filePath}\n")
                    skipped += 1

            log_file.write("\n--- Summary ---\n")
            log_file.write(f"Total photos processed: {len(photos)}\n")
            log_file.write(f"Moved: {moved}\n")
            log_file.write(f"Skipped: {skipped}\n")
            log_file.write(f"Failed: {failed}\n")
    else:
        print("No folder selected.")


if __name__ == "__main__":
    main()