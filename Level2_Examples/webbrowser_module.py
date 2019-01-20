# Opening a URL with Default Browser
import webbrowser

# To simply open a URL, use the open() method:
url = "http://Phika.ir"
webbrowser.open(url)

# open URLs in new windows:
webbrowser.open_new(url)

# Opening a new tab:
webbrowser.open_new_tab(url)


# NOTE
# open_new method is commonly ignored by modern browsers
# and the URL is usually opened in a new tab.
