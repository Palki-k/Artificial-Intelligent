import open_app
import webbrowser

def open_brain(text):
    if "website" in text or "open website named" in text:
        text=text.replace("website","").strip()  #to remove unwanted name we use strip
        text=text.replace("open website named","").strip()
        webbrowser.openweb(text)
    else:
         text=text.replace("app","").strip()
         open_app.open_app(text)


while True:
    x=input("hukum mere aaka")
    open_brain(x)