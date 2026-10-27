import os

def main():
    DirectoryName = input("Enter the name of Directory : ")
    
    print("Contents of the directory are : ")
    
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):   # os.walk(DirectoryName) is important
        print("FolderName : ",FolderName)
        
        for subf in SubFolderName:
            print("SubFolderName : ",subf)
        
        for fname in FileName:
            print("File name : ",fname)    
            
if __name__ == "__main__":
    main()