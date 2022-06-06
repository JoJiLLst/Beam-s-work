import os

folder = r"D:\jillzaza\Coding_area\Main project work\Code\Beam's work\Human face\\"
count = 1

for file_name in os.listdir(folder):
    
    source = folder + file_name

    destination = folder + "Humanface_" + str(count) + ".jpg"

    os.rename(source, destination)
    count += 1
print('All Files Renamed')
print('New Names are')
Mlg = os.listdir(folder)
print(Mlg)