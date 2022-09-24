# YAPS - Yet Another Phishing Site

# Libraries
import argparse, requests, os

# Parser Initialization
parser = argparse.ArgumentParser()

# Arguments
site = parser.add_argument("-s", "--site", help="Site", required=True)
data = parser.add_argument("-d", "--data", help="Data", required=True)
cookie = parser.add_argument("-c", "--cookie", help="Cookie <name=data>", required=False, default=None)
user_agent = parser.add_argument("-u", "--user-agent", help="User-Agent", required=False, default="")
header = parser.add_argument("-H", "--header", help="Header <name=data>", required=False, default=None)

# Read arguments from command line
args = parser.parse_args()

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
    if args.cookie:
        cookieArray = args.cookie.split("=")
        cookie = {cookieArray[0]: cookieArray[1]}
                
    # Check if user-agent is set
    if args.user_agent:
        user_agent = args.user_agent 
                
    # Check if header is set
    if args.header:
        headerArray = args.header.split("=")
        header = {headerArray[0]: headerArray[1]}

    # Input number of files based on number of post parameters
    for i in range(postCount):
        userInput = input("Enter target file for " + postArray[i][0] + ": ")
        # Check if file exists
        if os.path.isfile(userInput):
            # Check if file is empty
            if os.stat(userInput).st_size == 0:
                print("File is empty")
                exit(1)
            postArray[i].append(userInput)
        else:
            print("File not found. Exiting...")
            exit(1)
    
    
    print(postArray)
    
except Exception as e:
    print("Error : " + str(e))
    exit(1)
