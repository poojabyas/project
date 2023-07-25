import instaloader

# Use Profile class to access metadata of account
# Create an instance of Instaloader
loader = instaloader.Instaloader()
# Prompt the user to enter the Instagram username
username = input("Enter the Instagram username: ")
# Download the user's profile
loader.download_profile(username, profile_pic_only=False)
# Iterate over the user's posts and download them
for post in loader.get_profile_posts(username):
    loader.download_post(post, target=username)
print("Posts downloaded successfully!")









