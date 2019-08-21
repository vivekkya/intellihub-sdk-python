import intellihub


def save_img(response, filepath):
    with open(filepath, "wb") as f:
        f.write(response)


def main():
    c = intellihub.IntellihubClient('xxx')

    response = c.face_detection_image('../img/fd-actual-img.jpg')  # it will return image data in bytes.
    print(response)
    save_img(response, "../img/fd-response.png")
    response = c.face_detection_json('../img/fd-actual-img.jpg')  # it will return the co-ordinates of detected faces
    print(response)
    response = c.license_plate_detection_image('../img/lp-actual-img.jpg')  # it will return image data in bytes.
    save_img(response, "../img/lp-response.png")
    response = c.license_plate_detection_json(
        '../img/lp-actual-img.jpg')  # it will return the co-ordinates of detected licence plates.
    print(response)


if __name__ == '__main__':
    main()
