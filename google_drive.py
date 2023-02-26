from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth()



#Google_Drive

#Sending_File

class Sending_File:

    def __init__(self, folderName: str, parent_folderName: str, path_to_file: str, name: str) -> None:

        self.drive = GoogleDrive(gauth)
        self.parent_folder_id = None
        self.parent_folder_id = self.check(parent_folderName)
        self.folder_id = self.check(folderName)
        self.folderName = folderName
        self.path_to_file = path_to_file
        self.name = name
        self.upload_file()





    def check(self, folderName: str) -> str:
        file_list = self.drive.ListFile().GetList()
        fileID = None
        for id, file in enumerate(file_list):

            if (file['title'] == folderName) and not file['labels']['trashed']:
                fileID = file['id']  #get folder id
                break

            if id == len(file_list) - 1 and not fileID:
                self.create_folder(folderName)

                file_list_1 = self.drive.ListFile().GetList()
                for id, file in enumerate(file_list_1):
                    if(file['title'] == folderName):
                        fileID = file['id']  #get folder id
                        break

        return fileID





    def create_folder(self, folderName: str):
        folder_id = None
        if self.parent_folder_id:
            folder_id = {'id': self.parent_folder_id}

        file_metadata = {
            'title': folderName,
            'parents': [folder_id], #parent folder
            'mimeType': 'application/vnd.google-apps.folder'
        }

        folder = self.drive.CreateFile(file_metadata)
        folder.Upload()





    def upload_file(self):

        my_file = self.drive.CreateFile({'title': self.name, 'parents': [{'id': self.folder_id}]})
        my_file.SetContentFile(self.path_to_file) #путь до файла
        my_file.Upload()
        my_file.InsertPermission({
            'type': 'anyone',
            'value': 'anyone',
            'role': 'reader'})

        self.link = my_file['alternateLink']






    
if __name__ =='__main__':
    #m = Google_Drive('voice_3', 'voice_2')
    m = Sending_File('tavel_tava_42342', 'voice_5')

    print(m.__dict__)












