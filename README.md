# Reddit-Post-Remover
A script to remove existing Reddit posts and comments based on keywords.  
The account that runs this script must be a moderator in the subreddit.  

## Disclaimer
This script does not run continuously, and it does not scan incoming posts/comments.  
You can use the AutoModerator for those functions.

### Instructions
- Ensure you have Python installed on your system. You can download it here https://www.python.org/downloads/.
- Install the PRAW package ```pip install praw```.
- Create a Reddit App (script) at https://www.reddit.com/prefs/apps/ and get your specified keys.
- Store the python script and the details.ini file in the same folder.
- Edit the details.ini file with your details.
- Run the program ```python main.py```.
