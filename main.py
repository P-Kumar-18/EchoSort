from sorter import get_date_time, date_and_time, get_photos, EchoSort
from gui import app


def main():
    photos_folder = app()
    if photos_folder:
        photos = get_photos(photos_folder)
        moved = 0
        skipped = 0
        failed = 0
        with open("log.txt", "w", encoding="utf-8") as log_file:
            for fileName, filePath in photos:
                date_time = get_date_time(filePath)
                if date_time:
                    try:
                        date, time = date_and_time(date_time)
                        EchoSort(date, filePath, fileName, log_file)
                        moved += 1
                    except Exception as e:
                        log_file.write(f"Error parsing data for {filePath}: {e}\n")
                        failed += 1
                else:
                    log_file.write(f"Skipped no EXIF data for {filePath}\n")
                    skipped += 1
            log_file.write("\n---Summary---\n")
            log_file.write(f"Total photos processeed: {len(photos)}\nMoved: {moved}\nSkipped (No Exif Data): {skipped}\nFailed (Error while processing): {failed}")
    else:
        print("No folder Selected.")


if __name__ == "__main__":
    main()