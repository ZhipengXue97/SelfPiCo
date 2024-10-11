# Extracted from https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver
my_options = webdriver.ChromeOptions()
my_options.add_argument( '--disable-blink-features=AutomationControlled' )

