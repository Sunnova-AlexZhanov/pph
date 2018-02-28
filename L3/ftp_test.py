import datetime
import os
import tempfile

#from ftplib import FTP_TLS as egnyte_ftp
import paramiko




def fetch_files(given_date_time: datetime):

    host = "files.cleanpower.com"

    i = 1
    print('Opening Itron FTP... (%s/5)' % (i))
    transport = paramiko.SSHClient()
    transport.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    while True:
        try:
            transport.connect(hostname=host, username="SunnovaClient", password="SunnovaPDR!", timeout=5)
            break
        except paramiko.BadHostKeyException:
            raise paramiko.BadHostKeyError()
        except paramiko.AuthenticationException:
            raise paramiko.AuthenticationError()
        except Exception as ex:
            print('Could not connect, retrying...{}'.format(ex))
            i += 1
            #datetime.time.sleep(2)

        if i == 5:
            print('Was not able to connect to Itron FTP at %s. Exiting...', host)
            raise Exception('Was not able to connect to Itron FTP at %s. Exiting...', host)

    ftp = transport.open_sftp()
    file_list = ftp.listdir_attr()

    local_files = []
    print('Getting file from date: ' + str(given_date_time))
    for f in file_list:
        time_stamp = f.st_mtime
        file_name = f.filename
        file_date = datetime.datetime.fromtimestamp(time_stamp)

        #if given_date_time <= file_date:
        local_file_location = tempfile.gettempdir() + os.path.sep + file_name
        print('Copying file: ' + file_name + ' to ' + local_file_location)
        print(file_name, local_file_location)
        local_files.append(local_file_location)

        file = open(local_file_location, 'wb')
        print('Retrieving %s to %s', file_name, local_file_location)
#        ftp.prot_p()
        ftp.retrbinary('RETR ' + file_name, file.write)
        file.close()


    return local_files

if __name__ == "__main__":
    fetch_files(given_date_time=datetime.datetime.now())