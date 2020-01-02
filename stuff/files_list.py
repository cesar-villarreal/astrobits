import requests
from bs4 import BeautifulSoup

url = "http://cvillarreal.xyz/astrobits/stuff/download"
response_text = requests.get(url, params={}).text
links_delete = 5

def GetFilesList(url = url, links_delete = links_delete):
	soup = BeautifulSoup(response_text, 'html.parser')
	a = soup.find_all('a')
	list_files = [url+'/'+i.get('href') for i in a]


	for i in range(links_delete):
		del list_files[0]

	return list_files