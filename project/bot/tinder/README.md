# TinderBot

This is a script written in Python using the Selenium library to automate interactions with the Tinder website. The script allows you to automatically login to your Tinder account using your Facebook credentials, swipe right on profiles, send messages to matches, and perform other actions.

## Installation

To run this code, you need to have the following dependencies installed:

- Python (version 3.x)
- Selenium library
- ChromeDriver (for using Chrome browser)

You can install the Selenium library by running the following command:

```
pip install selenium
```

To install ChromeDriver, you can follow the instructions on their website: [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/)

## Usage

1. Make sure you have installed all the dependencies mentioned above.
2. Download the script file (`tinder_bot.py`) to your local machine.
3. Open the script file in a text editor or IDE of your choice.
4. Replace the `email` and `password` variables inside the `facebook_login()` method with your actual Facebook login credentials (or uncomment the import statement and use the credentials from an external file).
5. Save the file.
6. In the terminal or command prompt, navigate to the directory where the script file is located.
7. Run the script using the following command:

```
python tinder_bot.py
```

8. The script will open the Tinder website, login to your account, and start swiping right on profiles automatically. It will also send a message to any matches it finds.
9. You can customize the behavior of the bot by modifying the methods and adding additional functionality as needed.

Please note that automating interactions with websites may be against the terms of service of certain websites. Use this script responsibly and at your own risk.

Enjoy automating your Tinder experience!