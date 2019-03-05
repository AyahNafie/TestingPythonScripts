from ftplib import FTP

ftp = FTP('')
ftp.connect('192.168.10.254',21)
ftp.login('root','quectel123','')
ftp.cwd('/usrdata/files') #replace with your directory
ftp.retrlines('LIST')

def uploadFile(x):
 filename = x #replace with your file in your home folder
 ftp.storbinary('STOR '+filename, open(filename, 'rb'))
 ftp.quit()

def downloadFile(y):
 filename = y #replace with your file in the directory ('directory_name')
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

#uploadFile('TestFTP.txt')
downloadFile('demo.wav')
