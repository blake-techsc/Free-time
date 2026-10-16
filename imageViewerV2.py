import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Image Viewer")
        self.root.geometry("800x600")
        self.root.configure(bg="#222222")

        self.imageFiles = []
        self.index = 0
        self.photo = None

        self.imageLabel = tk.Label(
            root, bg="#222222"
        )
        self.imageLabel.pack(
            expand=True, fill="both", padx=10, pady=10
        )

        controls = tk.Frame(root, bg="#222222")
        controls.pack(pady=10)

        tk.Button(
            controls, text="Open Image",
            command=self.openImage
        ).pack(side="left", padx=5)

        tk.Button(
            controls, text="Previous",
            command=self.prevImage
        ).pack(side="left", padx=5)

        tk.Button(
            controls, text="Next",
            command=self.nextImage
        ).pack(side="left", padx=5)

        self.status = tk.Label(
            root, text="Open an image to start",
            bg="#222222", fg="white"
        )
        self.status.pack(pady=5)
        self.root.bind("<Left>", lambda event: self.prevImage())
        self.root.bind("<Right>", lambda event: self.nextImage())

    def openImage(self):
        path = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.gif *.webp"),
                ("All files", "*.*")
            ]
        )

        if not path:
            return

        folder = os.path.dirname(path)
        extensions = (".png", ".jpg", ".jpeg", ".gif", ".webp")

        self.imageFiles = sorted(
            os.path.join(folder, name)
            for name in os.listdir(folder)
            if name.lower().endswith(extensions)
        )

        self.index = self.imageFiles.index(path)
        self.showImage()

    def showImage(self):
        if not self.imageFiles:
            return

        path = self.imageFiles[self.index]

        try:
            image = Image.open(path)
            image.thumbnail((760, 480))

            self.photo = ImageTk.PhotoImage(image)
            self.imageLabel.configure(image=self.photo)

            self.status.configure(
                text=f"{os.path.basename(path)}  "
                     f"({self.index + 1}/{len(self.imageFiles)})"
            )
            self.root.title(
                f"Simple Image Viewer - {os.path.basename(path)}"
            )

        except Exception as error:
            self.status.configure(text=f"Could not open image: {error}")

    def nextImage(self):
        if self.imageFiles:
            self.index = (self.index + 1) % len(self.imageFiles)
            self.showImage()

    def prevImage(self):
        if self.imageFiles:
            self.index = (self.index - 1) % len(self.imageFiles)
            self.showImage()


if __name__ == "__main__":
    root = tk.Tk()
    viewer = ImageViewer(root)
    root.mainloop()
