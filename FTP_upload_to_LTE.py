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

uploadFile('TestFTP.txt')
