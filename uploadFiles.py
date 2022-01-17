import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def uploadFile(self, file_from , file_to ):
        dbx = dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from ):
            for file in files:
                local_path = os.path.join(root , file)
                relative_path = os.path.relpath(local_path , file_from)
                dropbox_path = os.path.join(file_to , relative_path)

                with open(local_path , 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path , mode=WriteMode('overwrite'))

def main():
    access_token = 'qqd9wDdFtuwAAAAAAAAAASYuHOp_kFpKdwqvhGTZy7_W2TCgjykdURwLAt63_sd9'
    transferData = TransferData(access_token)

    file_from = input('Enter the path of the file that you want to transfer : ')
    file_to = input('Enter the full path where you want to upload the file (including the file name) : ')

    transferData.upload_file(file_from , file_to)
    print('Transfer successful!')

main()
