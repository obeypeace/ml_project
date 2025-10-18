import os
import sys
import numpy as np
import pandas as pd
import dill
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            
    except Exception as e:
        raise CustomException(e, sys)
    
"""
def save_object(file_path, obj):
This defines a function that takes:
file_path: where you want to save the object (e.g. 'artifacts/model.pkl')
obj: the Python object you want to save (e.g. a trained model, scaler, or encoder)

2️⃣ dir_path = os.path.dirname(file_path)
Extracts the folder path (directory) from the full file path.
📘 Example:
file_path = 'artifacts/model.pkl'
dir_path = os.path.dirname(file_path)
print(dir_path)

Output: artifacts. So it isolates the folder name in case you need to create it.

3️⃣ os.makedirs(dir_path, exist_ok=True). Creates the folder if it doesn’t already exist.
exist_ok=True means: “don’t raise an error if it already exists.”
📘 Example:
If artifacts/ folder doesn’t exist, it will be created automatically.

4️⃣ with open(file_path, "wb") as file_obj:

Opens the file in write-binary mode ("wb").

This means the file will be created if it doesn’t exist.

file_obj is the file handle used to write to that file.

5️⃣ dill.dump(obj, file_obj)

This is where the magic happens ✨

dill is like an advanced version of pickle.

It serializes (converts) any Python object (even complex ones) into a byte stream and writes it to the file.

That way, you can load it back later using dill.load() and get the same Python object back in memory.
"""