# YAPS - Yet Another Phishing Site

# Libraries
import argparse, requests, os

# Parser Initialization
parser = argparse.ArgumentParser()

# Arguments
site = parser.add_argument("-s", "--site", help="Site", required=True)
data = parser.add_argument("-d", "--data", help="Data", required=True)
cookie = parser.add_argument("-c", "--cookie", help="Cookie <name=data>", required=False, default=None)
header = parser.add_argument("-H", "--header", help="Header Data", required=False, default=None)
timeout = parser.add_argument("-t", "--timeout", help="Timeout", required=False, default=1)

# Read arguments from command line
args = parser.parse_args()

# Variables
postArray = []

try:
    # Print Banner
    print('''
  ________________________________
  YAPS - Yet Another Phishing Site
  --------------------------------
         \   ^__^ 
          \  (oo)\_______
             (__)\       )\/
                 ||----w |
                 ||     ||''')
    
    
    # Check if site is up
    if requests.get(args.site).status_code == 200:
        pass

    # Post parameters
    postArray = args.data.split("&")
    postCount = len(postArray)

    # Find all post parameters
    for i in range(postCount):
        postArray[i] = postArray[i].split("=")

    # Check if cookie is set
    if args.cookie != None:
        cookieArray = args.cookie.split("=")
        args.cookie = {cookieArray[0]: cookieArray[1]}
                    
    # Check if header is set
    if args.header != None:
        headerArray = args.header.split("=")
        args.header = {headerArray[0]: headerArray[1]}
            
    # Check if timeout is set
    if args.timeout <= 1: 
        timeout = args.timeout

    # Input number of files based on number of post parameters
    for i in range(postCount):
        userInput = input("Enter target file for " + postArray[i][0] + " parameter: ")
        # Check if file exists
        if os.path.isfile(userInput):
            # Check if file is empty
            if os.stat(userInput).st_size == 0:
                print("File is empty")
                exit(1)
            # Add file to array
            file = open(userInput, "r")
            postArray[i][1] = file
        else:
            print("File not found. Exiting...")
            exit(1)
 
    # Send requests
    def sendRequest(data):
        print("Sending request... " + str(data))
        
        # Default
        if(args.cookie == None and args.header == None):   
            requests.post(args.site, data=data, timeout=timeout)
        elif(args.cookie != None and args.header == None):   
            requests.post(args.site, data=data, cookies=cookie, timeout=timeout)
        elif(args.cookie == None and args.header != None):        
            requests.post(args.site, data=data, headers=header, timeout=timeout)
        elif(args.cookie != None and args.header != None):
            requests.post(args.site, data=data, cookies=cookie, headers=header, timeout=timeout)    
    
    # Reading files
    while True:
        localDict = {} 
        
        for i in range(postCount):
            line = postArray[i][1].readline().strip()
            localDict[postArray[i][0]] = line
            if line == "":
                exit()

        sendRequest(localDict)
        localDict.clear()
    
except Exception as e:
    print("Error : " + str(e))
    exit(1)
