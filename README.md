# Reddit-Post-Remover
A script to remove existing Reddit posts and comments based on keywords.  
The account that runs this script must be a moderator in the subreddit.  

## Disclaimer
This script does not run continuously, and it does not scan incoming posts/comments.  
You can use the AutoModerator for those functions.

### Instructions
- Ensure you have Python installed on your system. You can download it here https://www.python.org/downloads/ (Add to PATH during the installation).
- Download the ZIP file of this repo (Click on ```Code``` -> ```Download ZIP```).
- Open your command prompt and change your directory to where you unzipped the files.
- Install the PRAW package ```pip install praw```.
- Create a Reddit App (script) at https://www.reddit.com/prefs/apps/ and get your ```client_id``` and ```client_secret```.
- Edit the ```details.ini``` file with your details.
- Run the program ```python main.py```.
