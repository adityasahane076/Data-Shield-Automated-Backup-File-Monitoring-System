import os

def DirectoryScanner(DirectoryName = "Marvellous"):
    
    Ret = os.path.exists(DirectoryName)
    
    if (Ret == False):
        print("Their is no such Directory")
        return
    
    print("Contents of the directory are : ")
    
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("FolderName : ",FolderName)
        
        for subf in SubFolderName:
            print("SubFolderName : ",subf)
        
        for fname in FileName:
            print("File name : ",fname)
    
def main():
    
    DirectoryName = input("Enter the name of Directory : ")
    
    DirectoryScanner(DirectoryName)
    
    
            
if __name__ == "__main__":
    main()