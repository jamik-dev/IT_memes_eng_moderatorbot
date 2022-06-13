import requests

url = "https://programming-memes-images.p.rapidapi.com/v1/memes"

headers = {
	"X-RapidAPI-Key": "cb6ee3d652mshdc9aa33b770f3dbp13922cjsn3c3ee519339b",
	"X-RapidAPI-Host": "programming-memes-images.p.rapidapi.com"
}

def memes_api():
	memes = []
	response = requests.request("GET", url, headers=headers)
	for object in response.json():
		memes.append(object['image'])
	return memes
	