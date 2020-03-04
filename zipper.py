import zipfile
import os 
  
def get_all_file_paths(directory): 
  
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename)
            if '.txt' in filepath and 'alarmLog.txt' not in filepath:
                file_paths.append(filepath)
    # returning all file paths
    return file_paths         
  
def archive(directory, date):  
    # calling function to get all file paths in the directory 
    file_paths = get_all_file_paths(directory)
  
    # writing files to a zipfile 
    with zipfile.ZipFile('logs/archive_%s.zip' % str(date), 'w', zipfile.ZIP_DEFLATED) as zip: 
        # writing each file one by one 
        for file in file_paths: 
            zip.write(file)
            os.remove(file)