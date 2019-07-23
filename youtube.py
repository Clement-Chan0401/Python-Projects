import webbrowser, pyperclip, sys

sys.argv

if len (sys.argv) > 1:
    search = ' '.join(sys.argv[1:])
else:
    search = pyperclip.paste()

webbrowser.open ('https://www.youtube.com/results?search_query=' + search)
