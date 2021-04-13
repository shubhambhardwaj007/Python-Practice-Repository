import pyttsx3
pyttsx3.speak("Welcome to my tools")
import os
print("\n")
print("PRESS 1:To open chrome")
print("PRESS 2:To open notepad")
print("PRESS 3:To open firefox")
print("PRESS 4:To open chrome")
p=input("ENTER YOUR CHOICE:")
if int(p) ==1:
  os.system("chrome")
elif int(p) ==2:
  os.system("notepad")
elif int(p) ==1:
  os.system("firefox")
elif int(p) ==1:
  os.system("chrome")
else:
 print("donot support")

