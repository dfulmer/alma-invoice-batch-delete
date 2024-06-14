# Alma Invoice Batch Delete

## Set up
The purpose of this software is to automatically delete batches of In Review invoices from Alma, the Library Services Platform.

These instructions will walk you through the process of setting up your computer to run the software, setting up a user in Alma to delete the invoices, and deleting the invoices.

## Configuration of your computer
These instructions assume that you are using Windows and you have Chrome installed as a browser.

Open PowerShell (Start Menu > PowerShell), type 'python' and press enter.
If you see something like this:
```
Python 3.12.3
>>>
```

then you have Python. Type ```quit()```. If you get taken to the Windows store, click on Get to get Python.

## Retrieve a Chrome Driver
Determine which version of Chrome you have by clicking on the three dots in the upper right hand corner > Help > About Google Chrome. It will say something like this: "Version 125.0.6422.113 (Official Build) (64-bit)"

Here are instructions to get a Chrome Driver after version 115:  
https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver  

Start here: https://developer.chrome.com/docs/chromedriver/downloads  
Click :consult the Chrome for Testing availability dashboard >   
https://googlechromelabs.github.io/chrome-for-testing/ >  
click Stable >  
https://googlechromelabs.github.io/chrome-for-testing/#stable  
Open the URL in a new browser window and a ChromeDriver will be downloaded in zip format. Extract the content and move the file called chromedriver.exe to the desired location. In this example, we are using a folder on our Desktop called 'ibd' so go ahead and create a folder on your desktop called 'ibd'. Now you should have a file called 'chromedriver.exe' in a folder called 'ibd' on your desktop: C:\Users\user\Desktop\ibd.

## Configuration in Alma
Set up an Internal user with the ability to delete invoices called "Alma Bot".

Users > All > Almabot  
Add User > Public  
First name: Alma  
Last name: Bot  
Primary identifier: almabot  
User group: Staff Level  
Expiration date: 07/01/2024  
Identifier type: Inst ID; Value: almabot@umich.edu  
Email types: check Work  
Email address: [whatever you want]  
Purge date: 07/01/2025  
Save

Now, add a password then click Save.  
Add role: Invoice Operator; Scope: University of Michigan; Status: Active; Save Role.  
Add role: Invoice Operator Extended; Scope: University of Michigan; Status: Active; Save Role.  

Now log into Alma as the new user you created.  
Make “Review (Invoice)” the first quick link by doing this:  
Click Acquisitions and the star next to “Review (Invoice)” to add the quick link.  
That makes Ctrl+Alt+1 the keyboard shortcut to Review (Invoice).  
Also click Results per page: 10 on the bottom of the page, so the page will load faster.  

## Run the program
Here is how to get started in PowerShell. We will create a virutal environment, install the Selenium package, and then we are ready to delete the invoices.

```
PS C:\Users\user> cd Desktop\ibd
PS C:\Users\user\Desktop\ibd> python -m venv venv
PS C:\Users\user\Desktop\ibd> .\venv\Scripts\Activate.ps1
(venv) PS C:\Users\user\Desktop\ibd>
```
Now you are in a virtual environment, denoted by the (venv) before the prompt. Once there give this command:
```
python -m pip install selenium
```

Finally, take a copy of the main.py file from this repository and paste it into the ibd folder on your desktop.  
You need to make a few changes to the file main.py:  
First, add the password for the user you created in Alma to this line, between the single quotes:
```
element.send_keys('')
```
Next, make sure that the ```driver.get``` line has the appropriate Alma environment (Sandbox/Production) or the appropriate Alma institution.  
Save your changes.  
You can now run the software with this command typed into PowerShell, followed by pressing Enter:
```
python main.py
```

## Tips
- At any time you can stop the program from running by pressing CTRL+c while in the PowerShell terminal.

- If you click in the browser opened by the software which has the message “Chrome is being controlled by automated test software.” the program may get messed up, but you may go about your day in other browser windows while the software is running.

- The program creates a log file which records when it started, ended, and the invoice number and vendor name of each invoice deleted.

- You need to avoid having your computer go to sleep during the invoice batch delete process. Although it may appear on your screen that your computer is active and performing activities that would prevent it from going to sleep, that is not the case, and when your computer falls asleep the software will stop.

## Clean up
Give this command in PowerShell to close the virtual environment:
```
deactivate
```
Go into Alma and make the Alma Bot user inactive once you are finished.
