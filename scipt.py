import requests
username = "user"
password = 'password'
myfile = "/full/path/to/myfile.csv"
url = "https://www.mydomain.com/file_upload.php"

files = {'file': open(myfile, 'rb')}

r = requests.post(url, files=files, auth=(username, password), verify=False)
print r.text
print r.status_code
