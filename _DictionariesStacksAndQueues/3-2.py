class BrowserHistory:
    def __init__(self):
        self.history_stack = []

    def visit(self, url):
        self.history_stack.append(url)

    def back(self):
        if self.history_stack:
            return self.history_stack.pop()  
        return None  

browser = BrowserHistory()
browser.visit("page1.com")
browser.visit("page2.com")
browser.visit("page3.com")

print(browser.back())  
print(browser.back()) 
print(browser.back()) 