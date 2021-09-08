import os
import requests


class gbooks():
    googleapikey="AIzaSyCZTjBs8aFQ3gHRfw_xr-MgAT105MDJD_U"

    def search(self, value):
        parms = {"q":value, 'key':self.googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        print (r.url)
        rj = r.json()
        print (rj["totalItems"])
        
        try:
            for i in rj["items"]:
              #print(type(repr(i["volumeInfo"]["language"])))
              # if repr(i["volumeInfo"]["language"]!="nl"):
              #    continue
              #print (repr(i["volumeInfo"]))
              # lan=repr(i["volumeInfo"]["readingModes"]["language"])
              title=repr(i["volumeInfo"]["title"])
              author=repr(i["volumeInfo"]["authors"])
              date=repr(i["volumeInfo"]["publishedDate"])
              description=repr(i["volumeInfo"]["description"])
              print (title,author,date,description)
        except:
            print ("cascou")
            pass
            
         #      try:
                #print (repr(i["volumeInfo"]["imageLinks"]["thumbnail"]))
          #  except:
           #     pass

if __name__ == "__main__":
    bk = gbooks()
##    bk.search()