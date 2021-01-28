from bs4 import BeautifulSoup
import requests
import webbrowser

url = input("URL: ")
site = requests.get(url)

#Change path based on chrome.exe file
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
browser = webbrowser.get('chrome')

print("~~~~~~~~~~\nSTATUS CODE: " + str(site.status_code) + "\n~~~~~~~~~~")

src = site.content

soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
imgs = soup.find_all("img")

print("~~~~~~~~~~Links~~~~~~~~~~")
for link in links:
    try:
    	print(link.attrs['href'])
    except:
    	print("An Error Occurred")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

print("\n~~~~~~~~~~Images~~~~~~~~~~")
for img in imgs:
	try:
		if(str(img.attrs['src'])[0:4] == "http"):
			image = str(img.attrs['src'])
		else:
			image = url + str(img.attrs['src'])
		print(image)
		browser.open_new_tab(image)
	except:
		print("An Error Occurred")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
