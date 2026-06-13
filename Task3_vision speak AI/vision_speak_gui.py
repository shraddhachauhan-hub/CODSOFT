import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from transformers import BlipProcessor, BlipForConditionalGeneration
import pyttsx3

 # LOAD AI MODEL

print("Loading AI Model...")

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

print("Model Loaded Successfully!")

engine = pyttsx3.init()

image_path = ""

# FUNCTIONS


def upload_image():
    global image_path

    image_path = filedialog.askopenfilename(
        filetypes=[
            ("Images", "*.jpg *.jpeg *.png *.bmp")
        ]
    )

    if image_path:
        img = Image.open(image_path)
        img.thumbnail((240, 240))

        photo = ImageTk.PhotoImage(img)

        image_label.config(image=photo)
        image_label.image = photo

        status_var.set("📷 Image Uploaded Successfully")


def generate_caption():

    if not image_path:
        messagebox.showwarning(
            "Warning",
            "Please upload an image first."
        )
        return

    status_var.set("⏳ Generating Caption...")
    root.update()

    image = Image.open(image_path).convert("RGB")

    inputs = processor(
        image,
        return_tensors="pt"
    )

    if caption_mode.get() == "Normal":

        output = model.generate(
            **inputs,
            max_new_tokens=20
        )

    else:

        output = model.generate(
            **inputs,
            max_new_tokens=50
        )

    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    if caption_mode.get() == "Detailed":
        caption = (
            "Detailed Description: "
            + caption.capitalize()
            + "."
        )

    caption_var.set(caption)

    status_var.set("✅ Caption Generated Successfully")


def save_caption():

    caption = caption_var.get()

    if not caption:
        messagebox.showwarning(
            "Warning",
            "Generate a caption first."
        )
        return

    with open(
        "captions.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(caption + "\n")

    messagebox.showinfo(
        "Saved",
        "Caption saved successfully."
    )

    status_var.set("💾 Caption Saved")


def speak_caption():

    caption = caption_var.get()

    if caption:
        engine.say(caption)
        engine.runAndWait()

        status_var.set("🔊 Caption Spoken")


# GUI

root = tk.Tk()
root.title("VisionSpeak AI")
root.geometry("900x600")
root.configure(bg="#1e1e1e")


# TITLE

title = tk.Label(
    root,
    text="🤖 VisionSpeak AI",
    font=("Segoe UI", 24, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title.pack(pady=(20, 5))

subtitle = tk.Label(
    root,
    text="Smart Image Caption Generator",
    font=("Segoe UI", 11),
    bg="#1e1e1e",
    fg="#cfcfcf"
)

subtitle.pack(pady=(0, 20))


# UPLOAD BUTTON

upload_btn = tk.Button(
    root,
    text="📂 Upload Image",
    command=upload_image,
    bg="#3b82f6",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=15,
    pady=8
)

upload_btn.pack(pady=10)


# IMAGE PREVIEW

image_label = tk.Label(
    root,
    bg="#1e1e1e"
)

image_label.pack(pady=10)


# CAPTION STYLE

caption_mode = tk.StringVar(
    value="Normal"
)

mode_frame = tk.Frame(
    root,
    bg="#1e1e1e"
)

mode_frame.pack(pady=10)

tk.Label(
    mode_frame,
    text="Caption Style:",
    bg="#1e1e1e",
    fg="white",
    font=("Segoe UI", 10)
).pack(side="left")

tk.Radiobutton(
    mode_frame,
    text="Normal",
    variable=caption_mode,
    value="Normal",
    bg="#1e1e1e",
    fg="white",
    selectcolor="#2d2d2d"
).pack(side="left", padx=5)

tk.Radiobutton(
    mode_frame,
    text="Detailed",
    variable=caption_mode,
    value="Detailed",
    bg="#1e1e1e",
    fg="white",
    selectcolor="#2d2d2d"
).pack(side="left", padx=5)

# GENERATE BUTTON


generate_btn = tk.Button(
    root,
    text="🚀 Generate Caption",
    command=generate_caption,
    bg="#22c55e",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=15,
    pady=8
)

generate_btn.pack(pady=10)


# CAPTION OUTPUT


caption_var = tk.StringVar()

caption_frame = tk.Frame(
    root,
    bg="#2d2d2d",
    padx=15,
    pady=10
)

caption_frame.pack(
    pady=15,
    padx=20,
    fill="x"
)

caption_label = tk.Label(
    caption_frame,
    textvariable=caption_var,
    font=("Segoe UI", 13),
    wraplength=700,
    justify="center",
    bg="#2d2d2d",
    fg="white"
)

caption_label.pack()


# STATUS


status_var = tk.StringVar()
status_var.set("Ready")

status_label = tk.Label(
    root,
    textvariable=status_var,
    bg="#1e1e1e",
    fg="#bdbdbd",
    font=("Segoe UI", 10)
)

status_label.pack(pady=5)


# ACTION BUTTONS

button_frame = tk.Frame(
    root,
    bg="#1e1e1e"
)

button_frame.pack(pady=10)

save_btn = tk.Button(
    button_frame,
    text="💾 Save Caption",
    command=save_caption,
    bg="#f59e0b",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=12,
    pady=6
)

save_btn.pack(
    side="left",
    padx=10
)

speak_btn = tk.Button(
    button_frame,
    text="🔊 Speak Caption",
    command=speak_caption,
    bg="#8b5cf6",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=12,
    pady=6
)

speak_btn.pack(
    side="left",
    padx=10
)


# FOOTER


footer = tk.Label(
    root,
    text="Developed by Shraddha Chauhan | AI Internship Project",
    font=("Segoe UI", 9),
    bg="#1e1e1e",
    fg="#808080"
)

footer.pack(side="bottom", pady=15)

root.mainloop()