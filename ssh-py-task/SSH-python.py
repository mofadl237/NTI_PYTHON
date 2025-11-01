import paramiko
import os

# Get remote agent connection data from user input
REMOTE_HOST = input("Enter remote host IP address: ")
USERNAME = input("Enter the remote host username: ")
PASSWORD = input(f"Enter the remote host password for {USERNAME}: ")

# Define remote and local paths
REMOTE_PATH = f"/home/{USERNAME}"
LOCAL_PATH = os.getcwd()  # Local working directory
SCRIPT_FILE = "requirement.sh"  # File to be sent to remote host

# Create SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(REMOTE_HOST, username=USERNAME, password=PASSWORD)

# Check if the file exists locally before uploading
if not os.path.exists(SCRIPT_FILE):
    print(f"[!] File {SCRIPT_FILE} not found in {LOCAL_PATH}")
    exit(1)

# Send shell script to remote host through SFTP protocol
sftp = ssh.open_sftp()
remote_script_path = f"{REMOTE_PATH}/{SCRIPT_FILE}"
sftp.put(SCRIPT_FILE, remote_script_path)
print(f"Uploaded {SCRIPT_FILE} to {REMOTE_HOST}")

# Give file execute permission and run it on the remote agent
commands = [
    f"chmod +x {remote_script_path}",
    f"bash {remote_script_path}"
]

for command in commands:
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read().decode(), stderr.read().decode())

# List the files created remotely after running the script
stdin, stdout, stderr = ssh.exec_command(f"ls -1 {REMOTE_PATH}")
files = stdout.read().decode().splitlines()
print("Files created remotely:")
for f in files:
    print("   ", f)

# to get the remote logsfile.txt locally
remote_file = f"{REMOTE_PATH}/logsfile.txt"
local_file = os.path.join(LOCAL_PATH, "logsfile.txt")

try:
    sftp.get(remote_file, local_file)
    print("Downloaded logsfile.txt successfully.")
except Exception as e:
    print(f"[!] Failed to download logsfile.txt: {e}")

# Close SFTP and SSH connections
sftp.close()
ssh.close()
print ("all is done ,congratulations!!")
