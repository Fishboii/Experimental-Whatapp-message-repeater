# WhatsappBomber
Will send multiple messages to someone through Whatsapp. Be warned this could lead to you getting blocked or potentially crash or slow down Whatsapp.\
You will need a valid phone number registered to Whatsapp, the Whatsapp app and an active internet connection for this to work. \
I do not take responsibility for any damages caused by this program. Use at your own risk. 

Typically ~100 messages sent at once will not be a problem, but Whatsapp will take some time to send them out. Any number of messages over around 500(?) will cause Whatsapp to run very slow. I am unsure of the exact number as I had to end the program prematurely because of the above reasons. 

Do note that the reciepient's name must be the one stored in your contacts. You can check them in the Whatsapp mobile app. \
This program is written using Python 3.7 with the selenium module. \
Before running the code, make sure you have selenium installed. \
If you have any questions, you can email me at juntaozhang0617@gmail.com. \
Important: You need to create a file with Chromedriver.exe on your computer. You can go to https://sites.google.com/a/chromium.org/chromedriver/downloads to get the latest version. You will then need to get the path of the file (Properties or More Info) and paste it into line 9 of the code.\
So the code should look like:\
driver = webdriver.Chrome(executable_path=r'C:\Users\junta\Desktop\Selenium drivers\Chromedriver.exe')\
\
And you would need to change it to:\
driver = webdriver.Chrome(executable_path=r' Your Chromedriver.exe path ')

# Instructions for entering your path
<ol>
  <li>Go tohttps://sites.google.com/a/chromium.org/chromedriver/downloads and download the latest version of Chromedriver
  <li>Unzip the file
  <li>Create a folder to store the .exe, I recommend the Desktop
  <li>Right click the folder and click Properties or More Info
  <li>You will then need to check the location of the file
  <li>Copy the location to your clipboard
  <li>Paste it over the location in the code, make sure the location ends with the Chromedriver.exe
  <li>If all is done correctly, the program should run.</li>
</ol>

# Instructions for the Bomber
<ol>
<li>Enter the group or receiver's name. 
<li>Enter the number of times you want to send the message. 
<li>Enter the message. 
<li>The program will open Whatsapp web , you will need to use your phone to scan the QR code. 
<li>After scanning the QR code, you will then need to hit enter on the program and it will automatically start sending messages after a few seconds</li>
<ol>
