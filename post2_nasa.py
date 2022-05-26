import requests
import urllib

#See what nasa api posted today, convert reponse to string
r = requests.get("https://api.nasa.gov/planetary/apod?api_key=Nhb2t3OMjStLRQuXqJhMVKhA9YMtI7YJ5GXpQ0Lz")
r = str(r.content)

#URL of photo is in the response, lets process.

#search location of HD photo tag then change to integer
hdloc = r.find("hdurl")
hdloc = int(hdloc) 

# get the url specifically without the tag, look for beginning and end
hdloc_end = r.find(",",hdloc+8)
r_url = r[hdloc+8:hdloc_end-1]
print(r_url)


