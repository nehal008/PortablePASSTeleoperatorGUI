# -*- coding: utf-8 -*-
from transformers import CLIPTextModel, CLIPTextConfig, CLIPProcessor, CLIPModel
import torch
from PIL import Image

import os
import pandas as pd
import numpy as np
import pyrebase
import math
import time
import transcribe as t


class Identify:
    """
    initializes the clip model using huggingface transformers
    """
    def __init__(self):
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    """
    imageList - list of images currently used by pepper
    filepath - name of directory containing all possible images
    
    get_images opens the filepath directory and constructs a list of image files to match the provided file names given by imageList
    """        
    def get_images(self, filepath):
        self.filepath = filepath
        file_names = []
        self.images = []
        for file in [file for file in os.listdir(self.filepath) if file.endswith(".png") or file.endswith(".jpg")]:
            image = Image.open(self.filepath + '/' + file)
            self.images.append(image)
            file_names.append(file)
        
        return file_names

    """
    text - string variable used to calculate probabilities
    uses the constructed self.images to encode text and images, returns the resulting cosine similarites and distance value
    """
    def encode(self, text):
        matrix = []
        inputs = self.processor(images=self.images,text=text, return_tensors="pt", padding=True)
        outputs = self.model(**inputs)
        
        logits_per_image = outputs.logits_per_text
        probs = logits_per_image.softmax(dim=1)
        probs = probs.data.numpy()
        
        matrix.append(probs)
        matrix = np.array(matrix)[:,0]
        distance = math.sqrt(np.trace(np.dot(matrix,matrix.T)))
        
        return distance, matrix
    
def find_top(matrix, precision):
    top = max(matrix[0])
    second = 0.00
    for val in matrix[0]:
        if second < val and val < top:
            second = val
            
    print(second / top)
            
    if (second / top) <= precision:
        return True
    else:
        return False
    

class Pyre:
    """initialize firebase with given creditials
    then create required stream and storage objects
    """
    def __init__(self):
        self.audioFile = "convert.mp3" 
        config = {
          "apiKey": "20e8a36028e30e74e31a97f555ab3aaef4b52278",
          "authDomain": "tammyagent-7dd0e.firebaseapp.com",
          "databaseURL": "https://tammyagent-7dd0e-default-rtdb.firebaseio.com/",
          "storageBucket": "tammyagent-7dd0e.appspot.com",
          "serviceAccount": r"C:\Users\parke\tammyagent-7dd0e-firebase-adminsdk-xhis7-20e8a36028.json"
        }
        
        firebase = pyrebase.initialize_app(config)
        
        self.storage = firebase.storage()
        self.db = firebase.database()
        self.imageStream = self.db.child("newImgPath").stream(self.imgHandler)
    
    """handler to be used by the database object"""
    def imgHandler(self, message):
        self.storage.child(message["data"]).download(self.audioFile)
        
    """grabs and downloads the most recently updated file in designated destination and downloads it"""
    def stream(self):
        self.imageStream = self.db.child("newImgPath").stream(self.imgHandler)
        return self.audioFile
            
    def __del__(self):
        self.imageStream.close()
        
if __name__ == '__main__':
 
    #define sets of images to send to CLIP
    setList = ["set1", "set2", "set3", "set4"]
    #define pyrebase object
    pullAudio = Pyre()
    
    for sets in setList:
        #list of images being used by pepper, should be retrieved from firebase
        #instance and perform member functions on clip-base object
        transcript = Identify()
        print("sets/"+sets)
        file_names = transcript.get_images("sets/" + sets)
        text = t.amazonTranscribe(pullAudio.stream(), "aws_key.txt")
        print(text)
        distance, matrix = transcript.encode(text)
        
        found = find_top(matrix, 0.1)
        if found:
            print("selected proper image")
        else:
            print("not sure of proper image")
            
        print(matrix)
        print(file_names)
        time.sleep(30)
        #save results in csv file
        #np.savetxt("test2.csv", matrix, delimiter=",")


    
    

