import glob
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox

class Image_Viewer:
    def __init__(self, root):
        self.window = root
        self.window.geometry("960x600")
        self.window.title('Image Viewer')
        self.window.configure(bg='white')
        self.window.resizable(width = False, height = False)

        self.img = img
        self.Image_Path = image_path
        
        self.Image_List = list()
        self.cur_index = 0

        self.width = 740
        self.height = 480

        # Creating Menubar
        self.menubar = Menu(self.window)
        # Adding Edit Menu and its sub menus
        edit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Open', menu=edit)
        edit.add_command(label='Open Image',command=self.open_image)
        edit.add_command(label='Open Images',command=self.open_images)
        edit.add_command(label='Open Folder',command=self.open_directory)

        # Adding About Menu
        about = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='About', menu=about)
        about.add_command(label='About', command=self.about_window)

        # Configuring the menubar
        self.window.config(menu=self.menubar)

        # Buttons
        prev_btn = Button(self.window, text="Prev", font=("Helvetica", 15, 'bold'), bg= '#FFDE59', command=self.prev_image)
        prev_btn.place(x=15,y=270)

        next_btn = Button(self.window, text="Next", font=("Helvetica", 15, 'bold'), bg='#FFDE59', command=self.next_image)
        next_btn.place(x=865,y=270)

        # Creating a Frame (#38B6FF)
        self.frame = Frame(self.window, bg='white',width=self.width,height=self.height)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5, rely=0.5)

            # Open an Image
    def open_image(self):
        self.reset()

        self.Image_Path = filedialog.askopenfilename(title = "Select an Image", filetypes = (("Image files", "*.jpg *.jpeg *.png"),))
        if len(self.Image_Path) != 0:
            self.Image_List.append(self.Image_Path)
            # Show the first image
            self.display_image(0)

    # Open Multiple Images
    def open_images(self):
        self.reset()

        self.Image_Path = filedialog.askopenfilenames(initialdir = "/", title = "Select Images", filetypes = (("Image files", "*.jpg *.jpeg *.png"),))
        if len(self.Image_Path) != 0:
            for path in self.Image_Path:
                self.Image_List.append(path)
            # Show the fisrt image
            self.display_image(0)

    # Open a directory
    def open_directory(self):
        self.reset()

        self.directory = filedialog.askdirectory()
        if self.directory != '':
            image_extensions = ['jpg', 'jpeg', 'png']
            for ext in image_extensions:
                for filename in glob.iglob(self.directory + f'**/*.{ext}', recursive=True):
                    self.Image_List.append(filename)

            self.display_image(0)
    
    # Displays the previous image   
    def prev_image(self):
        if self.cur_index > 0 and self.cur_index < len(self.Image_List):
            self.cur_index -= 1
            self.clear_screen()
            self.display_image(self.cur_index)
        # Image will display from the end
        else:
            self.cur_index = len(self.Image_List) - 1
            self.clear_screen()
            self.display_image(self.cur_index)

    # Displays the next image
    def next_image(self):
        if self.cur_index < len(self.Image_List) - 1:
            self.cur_index += 1
            self.clear_screen()
            self.display_image(self.cur_index)
        # Image will display from the start again
        else:
            self.cur_index = 0
            self.clear_screen()
            self.display_image(self.cur_index)

    def display_image(self, index):
        image = Image.open(self.Image_List[index])
        resized_image = image.resize((self.width, self.height))

        # Create an object of tkinter ImageTk
        self.img = ImageTk.PhotoImage(resized_image)

        # Create a Label Widget to display the text or Image
        label = Label(self.frame, image=self.img)
        label.pack()

    # Remove all widgets from the frame
    def clear_screen(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def reset(self):
        self.clear_screen()
        self.Image_List.clear()
        self.cur_index = 0

    # About window
    def about_window(self):
        messagebox.showinfo("Image Viewer", "Image Viewer;\nDeveloped by Blake")
    
    # It destroys the main GUI window of the application
    def Exit(self):
        self.window.destroy()

if __name__ == "__main__":
    root = Tk()
    img = None
    image_path = None
    obj = Image_Viewer(root)
    root.mainloop()