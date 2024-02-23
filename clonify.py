import os
import shutil
import re

def read_file():
    with open('./changes.txt', 'r') as file:
        target = file.readline().strip()
        inputs = file.readline().strip().split(',')
        return target, inputs

target, inputs = read_file()
print("Target String:", target)
print("Input Strings:", inputs)

def read_file():
    with open('./changes.txt', 'r') as file:
        target = file.readline().strip()
        inputs = file.readline().strip().split(',')
        return target, inputs

def process_files(target, inputs):
    for input_str in inputs:
        for filename in os.listdir('./input/'):
            if target.lower() in filename.lower():
                if target.islower():
                    new_filename = filename.replace(target, input_str.lower())
                elif target.istitle():
                    new_filename = filename.replace(target, input_str.capitalize())
                elif target.isupper():
                    new_filename = filename.replace(target, input_str.upper())
                else:
                    new_filename = filename.replace(target, input_str)

                shutil.copy(os.path.join('./input/', filename), os.path.join('./outputs/', new_filename))
                
                with open(os.path.join('./outputs/', new_filename), 'r+') as file:
                    content = file.read()
                    file.seek(0)
                    new_content = re.sub(target, lambda match: input_str if match.group().islower() else input_str.capitalize() if match.group().istitle() else input_str.upper() if match.group().isupper() else input_str, content, flags=re.IGNORECASE)
                    file.write(new_content)
                    file.truncate()

target, inputs = read_file()
process_files(target, inputs)

for filename in os.listdir('./input/'):
    shutil.move(os.path.join('./input/', filename), os.path.join('./outputs/', filename))