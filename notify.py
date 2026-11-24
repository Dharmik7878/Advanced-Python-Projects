from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title="RapTile Conding Industry",
            message="This is a notification from RapTile Conding Industry",
            timeout = 5,
        )
        time.sleep(60)  # Wait for 60 seconds before sending the next notification

#You can run this file in backgroung then open terminal and type the command:- "pythonw notify.py"KO