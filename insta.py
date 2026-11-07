# Instagram Bot program
from instabot import Bot

bot = Bot()
bot.login(username="ll_dharmik_18_ll", password="superman#7818")
bot.follow('deepika_pilli')
# bot.upload_photo("C:/Users/Dharmik/Downloads/IMG_20230610_123456.jpg", caption="My first post using !")
# bot.unfollow('deepika_pilli')

# followers = bot.get_user_followers('deepika_pilli')
# for follower in followers:
#     print(bot.get_user_info(follower))

# username = input("Enter your Instagram username: ")
# password = input("Enter your Instagram password: ")
#
# # Log in first
# if bot.login(
#     username=username,
#     password=password,
#     use_cookie=False):
#
#     print("Login successful!")
#
#     followers = bot.get_user_followers("deepika_pilli")
#     print(followers)
# else:
#     print("Login failed. Check the login message.")

# following = bot.get_user_following("deepika_pilli")
# for Following in following:
#     print(bot.get_user_info(Following))