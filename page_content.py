import requests
from hashlib import sha256
host = input("Enter the url to fetch: ")
req = requests.get("{}".format(host),headers={"accept":"text/html,application/xhtml+xml;q=0.9,image/webp,*/*,q=0.8","accept-encoding":"gzip, deflate, br","accept-language":"en-US,en;q=0.5","DNT":"0","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"})
print("Final url:{}".format(host))
print("SHA-256: {}".format(sha256(req.text.encode()).hexdigest()))
req2 = requests.get(host,headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"})
if sha256(req2.text.encode()).hexdigest() != sha256(req.text.encode()).hexdigest():
    print("The response is changing")
print("Data:\n")
print(req.text)
save = input("Save to file?")
if save == 'y':
    with open(input("Enter the file to save to:"),"w") as f:
        f.write(req.text)
        f.close()
        print("Saved")
    print("Saving...")
