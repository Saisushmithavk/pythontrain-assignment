from zipfile import ZipFile

zipObj = ZipFile('day4/sample.zip', 'w')
# Add multiple files to the zip
zipObj.write('day4/file.txt')
zipObj.write('day4/file.html')
# close the Zip File
zipObj.close()