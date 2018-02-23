from __future__ import print_function
from secret import CLIENT_SECRET_FILE, APPLICATION_NAME
import httplib2
import os
import sys
import yaml

from apiclient import discovery, errors
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive'
with open('conf.yaml') as f:
    conf = yaml.load(f)
    FOLDER_NAME = conf['folder']
    GDRIVE_DOC_ID = conf['gdrive']


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        print('hi')
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def print_file_content(service, file_id):
  """Print a file's content.

  Args:
    service: Drive API service instance.
    file_id: ID of the file.

  Returns:
    File's content if successful, None otherwise.
  """
  try:
    with open(os.path.join(FOLDER_NAME, 'article.md'), 'wb') as f:
      f.write(service.files().export(fileId=file_id, mimeType='text/plain').execute())
  except errors.HttpError as error:
    print('An error occurred: %s' % error)

def main():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    '''results = service.files().list(
                                pageSize=10,fields="nextPageToken, files(id, name)").execute()
                items = results.get('files', [])
                if not items:
                    print('No files found.')
                else:
                    print('Files:')
                    for item in items:
                        print('{0} ({1})'.format(item['name'], item['id']))'''

    print_file_content(service, GDRIVE_DOC_ID)

if __name__ == '__main__':
    main()
