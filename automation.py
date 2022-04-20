import cv2
import dropbox
import time
import random
start_time = time.time()

def takeSnapshot():
    number = random.randint(0, 100)
    problem = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame= problem.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")
    problem.release()
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = "sl.sl.BGH8giBCXylAUkxpdmLobV1HFtHOYDi1D7kYc5oXoW0KqehRN0iOWc7msHcrk_r9nOQW1hNpMZEdbUd4whPkEGVF4sUrvDnAFtJg1hcudXDGSf4EzEG2rXywDE4lM-uUm_cYFAmMrep2"
    file = img_counter
    file_from = file
    file_to = "/folder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 300):
            name = take_snapshot()
            upload_file(name)
main()