import tkinter as tk
from tkinter import messagebox
import customtkinter
import cv2
from deepface import DeepFace
from mtcnn import MTCNN

import os
import numpy as np
from PIL import Image
from numpy import asarray
from tkinter import ttk
from tkinter import Tk, filedialog
from PIL import Image, ImageTk

# import subprocess
# import time
# Function For Face Detection

"""# Function For Face Recognition"""

root1 = tk.Tk()
root1.title("Face Recognition Landing Page")

# Set the background color
root1.configure(bg='#f8f8f8')

# Create a frame for the content
content_frame = ttk.Frame(root1, padding=20)
content_frame.pack(expand=True, fill='both')

# Add the hand holding smartphone image
filename = 'logo.jpg'
image = Image.open(filename)
tk_image = ImageTk.PhotoImage(image)

hand_phone_label = ttk.Label(content_frame, image=tk_image, background='#f8f8f8')
hand_phone_label.pack(pady=20)

# Add the title
title_label = ttk.Label(content_frame, text="Smart Eye", font=('Arial', 24, 'bold'), background='#f8f8f8')
title_label.pack(pady=10)

# Add the subtitle
subtitle_label = ttk.Label(content_frame, text="Experience the future of security", font=('Arial', 16),
                           background='#f8f8f8')
subtitle_label.pack(pady=20)


# Add the "Get Started" button
def get_started():
    root1.destroy()

    root = tk.Tk()

    root.title("Face Recognition System")

    def detect_faces():
        print("Face detection button clicked")
        canvas1.delete("all")
        if not os.path.exists("detect_faces"):
            os.makedirs("detect_faces")
        filename = filedialog.askopenfilename()
            # filename = 'image.jpg'
        image = Image.open(filename)

        tk_image = ImageTk.PhotoImage(image)

        canvas1.create_image(0, 0, anchor=tk.NW, image=tk_image)
        canvas1.image = tk_image
            # load image from file
        pixels = cv2.imread(filename)
            # create the detector, using default weights
        detector = MTCNN()
            # detect faces in the image
        faces = detector.detect_faces(pixels)
            # To save the detectd faces
            # global face_array
            # global df

        def save_detect_faces(filename, result_list):

            i = 0

            for result in result_list:
                # get coordinates

                x, y, width, height = result['box']
                x2, y2 = x + width, y + height
                canvas1.create_rectangle(x, y, x2, y2, outline='red', width=2)

                face = filename[y:y2, x:x2]
                image = Image.fromarray(face)
                image = image.resize((224, 224))
                face_array = asarray(image)

                file_name = f'image_{i}.jpg'  # Generate a different file name for each image

                file_path = os.path.join('detect_faces', file_name)

                cv2.imwrite(file_path, face_array)

                i = i + 1

        save_detect_faces(pixels, faces)

    def recognize_faces():
        print("Face recognition button clicked")

        # folder_dir = "detect_faces"
        messagebox.showinfo("Select Folder 'detect_faces'", "Select detect_faces")
        folder_dir = filedialog.askdirectory(title="Select detect_faces Folder")
        messagebox.showinfo("Select Folder 'Database' ", "Select Database")
        folder = filedialog.askdirectory(title="Select Folder")
        detected = []
        not_detected = []
        for images in os.listdir(folder_dir):

            # check if the image ends with png
            print('images', images)
            file = os.path.join(folder_dir, images)
            print('file', file)
            x = cv2.imread(file)

            for images1 in os.listdir(folder):

                file_path = os.path.join(folder, images1)
                y = cv2.imread(file_path)
                type(y)
                type(x)
                result = DeepFace.verify(img1_path=x, img2_path=y, enforce_detection=False)
                print(result)
                i = 0
                if result['verified'] == True:
                    messagebox.showinfo("showinfo", f"Match Found between {images1} and {images} ")
                    print('detected')

                    print(detected.append(file_path))

        for k in detected:
            image = Image.open(k)
            image = image.resize((300, 300))
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(canvas2, image=photo)
            label.image = photo
            label_id = canvas2.create_window(i, 0, anchor=tk.NW, window=label)

            i += image.width

            i = i + 1

    def liveness():

        # Load images

        folder = filedialog.askdirectory(title="Select Database Folder")

        pan_card_image = cv2.imread("Pan-Card.jpg")

        for images in os.listdir(folder):
            # check if the image ends with png

            file = os.path.join(folder, images)
            c = cv2.imread(file)
            print(c)

            # Perform face recognition
            result = DeepFace.verify(pan_card_image, c, model_name='Facenet', distance_metric='euclidean_l2',
                                     enforce_detection=False)
            print(result)

            # Check if faces match
            if result['verified']:
                messagebox.showinfo("showinfo", f"Match found with {c}")
                image = Image.open(c)
                image = image.resize((300, 300))
                photo = ImageTk.PhotoImage(image)
                label = tk.Label(canvas2, image=photo)
                label.image = photo
                label_id = canvas3.create_window(i, 0, anchor=tk.NW, window=label)

                print("Faces match.")
            else:
                messagebox.showinfo("showinfo", "Match Not Found")
                print("Faces do not match.")

    def help_button_event():
        messagebox.showinfo("Quick Start Guide", "Step 1: Click on the Detect_faces Button then choose the particular image from wihch you want to detect the faces, Then choose the detect_faces folder and the database folder accordingly\n\nOur algorithm will detect the human faces inside the image you chosen\n\nStep 2: Click on the Recognize_faces button, our program will compare the detected faces with the database folder,\nif there is any match,\nit will show in the next canvas which faces are detected\n\nStep 3: If you want to check your image with any identity card click on card_biomatric button then choose database folder,\nour program will check if there is any match with the identity card and the databse images,\nit will show in the next canvas")

    def about_button_event():
        # root2 = tk.Tk()
        # image2 = tk.Label(root2, text="hello")
        # image2.pack()
        pass
        


    # Main Section Frame with Face Detection and Recognition Buttons

    left_frame = tk.Frame(root, width=200, height=400, bg='bisque2')
    left_frame.pack(side='left', fill='both', expand=True)

    middle_frame = tk.Frame(root, width=100, height=400, bg='PeachPuff2')
    middle_frame.pack(side='left', fill='both', expand=True)

    right_frame = tk.Frame(root, width=200, height=400, bg='bisque2')
    right_frame.pack(side='left', fill='both', expand=True)

    canvas1 = tk.Canvas(right_frame, width=600, height=250, bg='white')
    canvas1.pack(pady=10)

    detect_button = ttk.Button(middle_frame, text="Detect Faces", command=detect_faces)
    detect_button.place(x=10, y=100)

    canvas2 = tk.Canvas(right_frame, width=600, height=250, bg='white')
    canvas2.pack(pady=10)

    recognize_button = ttk.Button(middle_frame, text="Recognize Faces", command=recognize_faces)
    recognize_button.place(x=10, y=400)

    canvas3 = tk.Canvas(right_frame, width=600, height=250, bg='white')
    canvas3.pack(pady=10)

    Card_Biometric = ttk.Button(middle_frame, text="Card Biometric ", command=liveness)
    Card_Biometric.place(x=10, y=600)

    help = ttk.Button(left_frame, text="How To Use", command=help_button_event)
    help.place(x=10, y=50)

    subscribe = ttk.Button(left_frame, text="Subscribe??")
    subscribe.place(x=10, y=200)

    about = ttk.Button(left_frame, text="About Us", command=about_button_event)
    about.place(x=10, y=400)

    root.mainloop()


get_started_button = ttk.Button(content_frame, text="Get Started", command=get_started, style='Primary.TButton')
get_started_button.pack()

# Style the button
s = ttk.Style()
s.configure('Colorful.TButton', background='#007bff', foreground='white', font=('Arial', 12, 'bold'), padding=(10, 5))

root1.mainloop()

