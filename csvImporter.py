import gdata.docs.data
import gdata.docs.client
import gdata.docs.service
import gdata.spreadsheet.service
import getpass

user = raw_input('Please enter your username: ')
pw = getpass.getpass()
source = 'melange-gsoc-v1'
gd_client =  gdata.docs.service.DocsService()
gd_client.ClientLogin(user, pw, source=source)

file_path = raw_input('Enter path to csv file: ')

title = raw_input('Enter name of the spreadsheet: ')
content_type = gdata.docs.service.SUPPORTED_FILETYPES['CSV']
ms = gdata.MediaSource(file_path=file_path, content_type=content_type)

entry = gd_client.Upload(ms, title)

if entry:
      print('Upload successful!')
      print('Document now accessible at:', entry.GetAlternateLink().href)
else:
    print('Upload error.')


