# Discord-Meme-Bot
A simple discord bot that gets you memes from Google.

### bot.py
Runs the actual discord bot. 'TOKEN' is your discord project's token. The bot only responds to messages with a preceding '>' in a channel called 'memes'. 

### memes.py
Sends a Google search query using BeautifulSoup to get the requested category of memes, if none specified, just gets image results for 'memes'.
Downloads the images as a png file called 'meme.png' and this can be adjusted in the 'name_of_file' variable. All available meme categories are stored in the 'categories' list and more items can be added to it to allow for a wider range of topics.

**NOTE**: The images are enlarged by a scale factor of 2 because they are quite small when fetched from Google. They are still quite pixelated, and in some cases extremely hard to read. I tried finding an efficient way to upscale them, but was not successful - any solutions to this are much welcome...
