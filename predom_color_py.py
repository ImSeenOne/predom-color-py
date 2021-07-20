import cv2
from sklearn.cluster import KMeans
from scipy.spatial import KDTree
import json
import requests
from matplotlib import colors as matcolors
from tkinter import Canvas, messagebox
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
from datetime import datetime

COLORS_TO_FIND = 5

def openFile():
    filepath = filedialog.askopenfilename(filetypes=[("images", ".jpg .jpeg .png")])

    w = Canvas(root, width=500, height=400)
    w.create_text((250, 50), text="Procesando imagen...")

    print("Processing image...")

    clusters = COLORS_TO_FIND
    dc = DominantColors(filepath, clusters) 
    colors = dc.dominantColors().tolist()

    print("Colors were found...")
    now = datetime.now()

    f = open("Colors-genrtd-"+now.strftime("%d-%m-%Y-%H%M%S")+".txt", "w")

    x0 = 0
    y0 = 0
    x1 = 100
    y1 = 100

    j = 1

    for i in colors:
        color = dc.rgb2names(i)

        w.create_rectangle(x0, y0, x1, y1, fill=color.hex_value, outline = 'black')
        w.create_text((x1-50, y1+15), text=color.name+"\n"+color.hex_value)

        f.write("\nColor #"+str(j)+"\n\tName: "+color.name+"\n\tColor (HEX): "+color.hex_value+"\n\tClosest named value (HEX): "+color.closest_named_value)
        j+=1

        x0+=100
        x1+=100
    
    f.close()
    w.pack()
    messagebox.showinfo("Archivo de colores creado", "Los colores están almacenados en el archivo llamado:"+"Colors-genrtd-"+now.strftime("%d-%m-%Y-%H%M%S")+".txt")

class Color:
    
    name = None
    closest_named_value = None
    hex_value = None

    def __init__(self, name, closest_named_value, hex_value):
        self.name = name
        self.hex_value = hex_value
        self.closest_named_value = closest_named_value

    def toJSON(self):
        dataset = {"name": self.name, "hex": self.hex_value, "closest_named_value": self.closest_named_value}
        return json.dumps(dataset)
    
    def __str__(self):
        return "Name: "+str(self.name)+"\tHEX: "+str(self.hex_value)+"\tClosest named HEX:"+str(self.closest_named_value)

class DominantColors:

    CLUSTERS = None
    IMAGE = None
    COLORS = None
    LABELS = None
    
    def __init__(self, image, clusters=3):
        self.CLUSTERS = clusters
        self.IMAGE = image
        
    def dominantColors(self): # 
    
        #read image
        img = cv2.imread(self.IMAGE)
        
        #convert to rgb from bgr
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                
        #reshaping to a list of pixels
        img = img.reshape((img.shape[0] * img.shape[1], 3))
        
        #save image after operations
        self.IMAGE = img
        
        #using k-means to cluster pixels
        kmeans = KMeans(n_clusters = self.CLUSTERS)
        kmeans.fit(img)
        
        #the cluster centers are our dominant colors.
        self.COLORS = kmeans.cluster_centers_
        
        #save labels
        self.LABELS = kmeans.labels_
        
        #returning after converting to integer from float
        return self.COLORS.astype(int)

    @staticmethod
    def rgb2names(rgb_tuple):

        request = requests.get("http://thecolorapi.com/id?rgb="+str(rgb_tuple[0])+","+str(rgb_tuple[1])+","+str(rgb_tuple[2])+"&format=json")
        jdata = json.loads(request.text)
        return Color(jdata['name']['value'],jdata['name']['closest_named_hex'], '#%02x%02x%02x' % (rgb_tuple[0], rgb_tuple[1], rgb_tuple[2]))

root = tk.Tk()
root.geometry("500x300")
root.title("Py Dominant Colors by Cris Ramirez")
buttonSearch = tk.Button(root, text="Buscar imagen", command = openFile)
buttonSearch.pack()
root.mainloop()
