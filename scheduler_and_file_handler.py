import json 
import os, time
import schedule


# Dumb data in Json
def write_json(data, file='data.json'): 
    with open(file,'w') as f: 
        json.dump(data, f, indent=4) 


# Previous Files
previous_files = []

# Get files info and call write_json()
def job():  
    current_files = os.listdir('files_folder')
    
    global previous_files
    
    for file in current_files:
        if file in previous_files:
            pass
        else:
            file_info = {}
            (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat("files_folder\\" + file)

            file_info["Date Created"] = time.ctime(ctime) # Date Created
            file_info["Date Modified"] = time.ctime(mtime) # Date Modified
            file_info["File Name"] = file  # File name
            file_info["File Extension"] = file.split(".")[-1] # file extension
            file_info["Size(bytes)"] = size  # file size
            

            previous_files.append(file)
            
            with open('data.json') as json_file: 
                data = json.load(json_file) 

                temp = data['files_detail'] 
                temp.append(file_info) 
                
            write_json(data)
            file_info = {}
            
            print(file + " added in json.")
            

job()

# Scheduler Scan in every one minute
schedule.every().minutes.do(job)

while True:
    print("Scanning....')
    schedule.run_pending()