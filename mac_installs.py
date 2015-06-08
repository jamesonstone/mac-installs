#!/bin/python

"""
Before running this script you'll have to install the following:
"pip" (python package manager): 'sudo easy_install pip'
"""

import wget

ANDROID_STUDIO='https://drive.google.com/open?id=0B6sJjN90STveTEVPME9FWXRKaEU&authuser=0'
CRASHLYTICS='https://drive.google.com/open?id=0B6sJjN90STveRTl1dTZkOXBfVHM&authuser=0'
CRASHLYTICS_AS_PLUGIN='https://drive.google.com/open?id=0B6sJjN90STvedlBKb3FaTENpX0E&authuser=0'
GENYMOTION='https://drive.google.com/open?id=0B6sJjN90STvedlBKb3FaTENpX0E&authuser=0'
VIRTUAL_BOX='https://drive.google.com/open?id=0B6sJjN90STveemVua2I3a2ZDQkE&authuser=0'
SUBLIME_TEXT='https://drive.google.com/open?id=0B6sJjN90STveSV81alJYREI1NDA&authuser=0'
APPIUM_GUI='https://drive.google.com/open?id=0B6sJjN90STvecUh5T1lhempUSFE&authuser=0'
PYCHARM='https://drive.google.com/file/d/0B6sJjN90STveSkNTYkdDc015NW8/view?usp=sharing'
INTELLIJ='https://drive.google.com/open?id=0B6sJjN90STveYzRBdDU1N3dJTE0&authuser=0'
JAVA='https://drive.google.com/open?id=0B6sJjN90STveMjFSSHVESEd0ZUE&authuser=0'
JDK='https://drive.google.com/open?id=0B6sJjN90STveb2dLcktxMUJtVXc&authuser=0'
CHARLES='https://drive.google.com/open?id=0B6sJjN90STveNVQ1QTc0LWVTVk0&authuser=0'


download_links = {
    'Android Studio': ANDROID_STUDIO,
    'GenyMotion': GENYMOTION,
    'SublimeText': SUBLIME_TEXT,
    'Appium GUI': APPIUM_GUI,
    'PyCharm': PYCHARM,
    'IntelliJ': INTELLIJ,
    'Crashlytics': CRASHLYTICS,
    'Crashlytics as Plugin': CRASHLYTICS_AS_PLUGIN,
    'Java': JAVA,
    'JDK': JDK,
    'Charles': CHARLES,
    'Virtual Box': VIRTUAL_BOX,
    }


def download_files(answer, download_list):
    if answer == 'y' or answer == 'yes':
        for item in download_list:
            print item
            wget.download(download_list[item])
    else:
        print 'Thank you and have a really great day!'



def main():
    a = raw_input('Welcome to iHR Test Engineering setup. Would you like to start? ')
    download_files(a, download_links)
    print('All done! Please run each respective installer.')
    #webbrowser.open('https://github.com/appium/python-client')
    #webbrowser.open('http://www.seleniumhq.org/docs/')



if __name__ == '__main__':
    main()




