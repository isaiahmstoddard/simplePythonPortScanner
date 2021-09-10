import socket
import subprocess
import sys
from datetime import datetime

# Declare var for use later
remote_ip = ""

# Optional clearing of the screen
subprocess.call('clear', shell=True)

# Print banner
print("""

    __  __           _              ____       _ _   _     _
   |  \/  | __ _ ___| |_ ___ _ __  |  _ \  ___(_) |_| |__ ( )___
   | |\/| |/ _` / __| __/ _ \ '__| | | | |/ _ \ | __| '_ \|// __|
   | |  | | (_| \__ \ ||  __/ |    | |_| |  __/ | |_| | | | \__\\
   |_|  |_|\__,_|___/\__\___|_|    |____/ \___|_|\__|_| |_| |___/
    ____            _     ____                                  
   |  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
   | |_) / _ \| '__| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
   |  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |   
   |_|   \___/|_|   \__| |____/ \___\__,_|_| |_|_| |_|\___|_|   
                                    

""")

# Asking for the client to scan
print("Enter scan address format:\n\n")
print("(a) Enter URL to resolve \n(b) Enter IP to use\n\n")
userAddressChoice = str(input("> "))

if userAddressChoice.lower() == 'a':
    useraddress = str(input("Enter address: "))
    remote_ip = socket.gethostbyname(useraddress)
elif userAddressChoice.lower() == 'b':
    remote_ip = str(input("Enter IP address: "))
else:
    sys.exit("incorrect option entered")

print("\nRemote IP: " + remote_ip)

# Print banner
print('\n'+'-'*60)
print("Please wait, scanning remote host", remote_ip + "...")
print('-'*60)

# Get start time
t1 = datetime.now()

# using range to specify ports to scan
try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remote_ip, port))
        if result == 0:
            print("Port {}:     Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed CTRL+C")
    sys.exit()

except socket.gaierror:
    print("Hostname couldn't be resolved. Exiting...")
    sys.exit()

except socket.error:
    print("Couldn't connect. Exiting...")
    sys.exit()

# get end time
t2 = datetime.now()

# get final time amount
finalTime = t2-t1

print("Scanning completed in: ", finalTime)


