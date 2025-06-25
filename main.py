import tkinter as t
from tkinter import filedialog
import customtkinter as ctk
import cv2

root = ctk.CTk()
ro=t.Tk()
ro.withdraw()

frame = ctk.CTkFrame(root)

frame.pack(expand=True)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
root.geometry("500x500")
root.title("🌟 Smart Image Cropping Tool 🌟")
crop = None
name = None

def save():
    global crop,name
    n = name.get()

    if n.strip() is not None:
       full_name = n + ".jpg"
       cv2.imwrite(f"{full_name}",crop)
       label = ctk.CTkLabel(frame,text=f"✅ {full_name} Successfully Saved :) !!", text_color="lightgreen", font=("Arial", 14, "bold"))
       label.grid(row=7,column=0,pady=20,columnspan = 2)
    else:
       error_label = ctk.CTkLabel(frame, text="⚠ Please enter a valid name!", text_color="red", font=("Arial", 13))
       error_label.grid(row=6, column=0, pady=15)
   


def crop_image():
    b1.grid_forget()
    global crop,name
    file_path = filedialog.askopenfilename(title="Select the image", filetypes=[("Image Files",("*.jpg","*.jpeg","*.png"))])
    r=cv2.imread(file_path,1)
    sel=cv2.selectROI("Crop the image",r,fromCenter=False,showCrosshair=True)
    x,y,w,h = sel
    if w==0 or h==0 or x==0 or y==0:
      print("No region")
    else:
      crop=r[int(y):int(y+h),int(x):int(x+w)]
    cv2.imshow("Cropped Image",crop)
    cv2.namedWindow("Crop")
    cv2.waitKey(1000)
    cv2.destroyWindow("Crop")

    

    label = ctk.CTkLabel(frame,text=f"📂 Enter the File Name without Extension !!", text_color="lightgreen", font=("Arial", 30, "bold"))
    label.grid(row=2,column=0,pady=20,columnspan = 2)
    name = ctk.CTkEntry(frame,placeholder_text="📂 Enter the File Name without Extension", width=300, height=35, font=("Arial", 13))
    name.grid(row=3,column=0,pady=20)

    b2 = ctk.CTkButton(frame,text="💾 Click to Save",command=save, fg_color="Red", hover_color="Green", font=("Arial", 25, "bold"), corner_radius=20)
    b2.grid(row=8,column=0,pady=10)
    

b1 = ctk.CTkButton(frame,text="🖼 Select the image For Cropping !!",command=crop_image,fg_color="Blue", hover_color="Green", font=("Arial", 20, "bold"), corner_radius=15)
b1.grid(row=5,column=0,pady=40)

root.mainloop()
