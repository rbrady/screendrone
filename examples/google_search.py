# The MIT License (MIT)
#
# Copyright (c) 2016 Ryan Brady
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from screendrone import *


# set the stage
browser = webdriver.Firefox()
browser.get("http://www.google.com/")
time.sleep(2)

# roll sound
narrator = ESpeakNarrator({})

# action
with Movie(browser, CameraType, 'demo.ogv') as movie:
    script = ("This is an example demonstration of how to search google to"
              " find more information about python screencasting.")
    with Scene(script, narrator) as scene:
        search = browser.find_element_by_name('q')
        search.send_keys("python screencasting")
        search.send_keys(Keys.RETURN)  # hit return after you enter search text
        time.sleep(10)  # sleep for 10 seconds so you can see the results
        browser.quit()
