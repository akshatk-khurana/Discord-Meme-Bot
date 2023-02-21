# Discord-Meme-Bot
A simple discord bot that gets you memes from google.

### bot.py
Runs the actual discord bot. 'TOKEN' is your discord project's token. The bot only responds to messages with a preceding '>' in a channel called 'memes'. 

### memes.py
Sends a Google search query using BeautifulSoup to get the requested category of memes, if none specified, just gets image results for 'memes'.
Downloads the images as a png file called 'meme.png' and this can be adjusted 
