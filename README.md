Will send multiple messages to someone through Whatsapp.\
You will need a valid phone number registered to Whatsapp, the Whatsapp app and an active internet connection for this to work. \

Do note that the reciepient's name must be the one stored in your contacts. You can check them in the Whatsapp mobile app. \
This program is written using Python 3.7 with the selenium module. \
Before running the code, make sure you have selenium installed. \\
Important: You need to create a file with Chromedriver.exe on your computer. You can go to https://sites.google.com/a/chromium.org/chromedriver/downloads to get the latest version. You will then need to get the path of the file (Properties or More Info) and paste it into line 9 of the code.\
The code should look like:\
driver = webdriver.Chrome(executable_path=r'YOURPATHHERE')\
\
And you would need to change it to:\
driver = webdriver.Chrome(executable_path=r' Your Chromedriver.exe path ')
  
# Instructions for entering your path
<ol>
  <li>Go to https://sites.google.com/a/chromium.org/chromedriver/downloads and download the latest version of Chromedriver
  <li>Unzip the file
  <li>You will then need to check the location of the file
  <li>Copy the location to your clipboard
  <li>Paste it over the location in the code, make sure the location ends with the Chromedriver.exe
  <li>If all is done correctly, the program should run.</li>
</ol>

# Instructions
<ol>
<li>Enter the group or receiver's name. 
<li>Enter message repeat number
<li>Enter the message. 
<li>The program will open Whatsapp web , you will need to use your phone to scan the QR code. 
<li>After scanning the QR code, you will then need to hit enter on the program and it will automatically start sending messages after a few seconds</li>
<ol>
