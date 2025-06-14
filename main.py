from sorter import get_date_time, date_and_time, get_photos, EchoSort


def main():
    photos_folder = "photos"
    photos = get_photos(photos_folder)

    for fileName, filePath in photos:
        date_time = get_date_time(filePath)
        date, time = date_and_time(date_time)
        EchoSort(date, filePath, fileName)


if __name__ == "__main__":
    main()