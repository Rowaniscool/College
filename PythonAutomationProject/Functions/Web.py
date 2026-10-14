import requests
import webbrowser
from bs4 import BeautifulSoup

class Web:
    def __init__(self, ui):
        self.ui = ui
        self.ui.getStatusCode.clicked.connect(self.getStatusCode)
        self.ui.openWebsite.clicked.connect(self.openSite)
        self.ui.scrapeWebsite.clicked.connect(self.scrapeSite)


    def getStatusCode(self):
        self.ui.webOutPut.clear()
        siteInput = self.ui.websiteInput.text()
        try:
            code = requests.get(f"https://{siteInput}")
            self.ui.webOutPut.insertPlainText(f"Status code: {code.status_code}\n")
            if code.status_code == 200:
                self.ui.webOutPut.insertPlainText("Website is up")
            else:
                self.ui.webOutPut.insertPlainText("Website is down or cant reach it")
        except:
            self.ui.webOutPut.insertPlainText("Website is unreachable/down")


    def openSite(self):
        website = f"https://{self.ui.websiteInput.text()}"
        if website == "https://":
            self.ui.webOutPut.clear()
            self.ui.webOutPut.insertPlainText("Enter a website name")
        else:
            webbrowser.open_new_tab(website)


    def scrapeSite(self):
        self.ui.webOutPut.clear()
        website = f"https://{self.ui.websiteInput.text()}"
        status = requests.get(website)

        if status.status_code == 200:
            soup = BeautifulSoup(status.text, "html.parser")
            text = soup.get_text("\n", strip=True)
            self.ui.webOutPut.insertPlainText(text)

        else:
            self.ui.webOutPut.insertPlainText("Website unreachable")
