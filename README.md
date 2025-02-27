# TopProcesses
# A cross-compatible python script that will check for the top processes that are consuming the most CPU or Memory resources.
# Developed by Arman "The Automator" Vakili. 
# Contact: ArmanTheAutomator@gmail.com

Top Processes by CPU or Memory - README


**📌 Overview**
This Python script allows users to monitor and manage the top 5 processes consuming the most CPU or Memory on their system. It provides an interactive interface to:
✅ View the most resource-intensive processes.
✅ Choose between CPU or Memory usage tracking.
✅ Optionally terminate a process directly from the script.


**🛠️ Requirements**
The script uses Python 3 and requires the following dependencies:
psutil → For retrieving system process information.
os → For terminating processes.
🔹 If psutil is not installed, install it using:

pip install psutil


**⚙️ How It Works**
1️⃣ User Input: The script asks the user to choose whether to monitor CPU or Memory usage.
2️⃣ Process Listing: It retrieves and displays the top 5 processes sorted by usage.
3️⃣ Process Termination Option: The user can enter a number (1-5) to terminate a process or enter 0 to exit.


**🚀 Running the Script**
Run the script using:

python 2_TopProcesses.py


**📌 Example Run**

Enter 'cpu' to monitor CPU usage or 'memory' to monitor memory usage: cpu
Top 5 processes by CPU usage:
1. chrome.exe - 27.5% CPU
2. python.exe - 18.2% CPU
3. explorer.exe - 5.1% CPU
4. vscode.exe - 2.4% CPU
5. discord.exe - 1.8% CPU

Enter the number (1-5) of the process to terminate, or '0' to quit: 2
Process python.exe terminated successfully.


**🔹 Error Handling & Edge Cases**
If invalid input is entered (e.g., selecting "disk" instead of "cpu" or "memory"), an error is shown.
If a process cannot be terminated (due to permissions), a message is displayed.
If the user enters an invalid process number, they are prompted again.


**🛠️ Compatibility**
✅ Windows → Works with standard Windows processes.
✅ Linux & macOS → Works with system processes but may require sudo for terminating system-owned tasks.


**📌 Notes**
Some system processes cannot be terminated without admin privileges.
The script uses soft termination (SIGTERM), but you can modify it to force-kill using SIGKILL (9).

