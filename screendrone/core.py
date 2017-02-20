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
from threading import Thread


class Movie(object):

    def __init__(self, browser, filename):
        window_pos = browser.get_window_position()
        window_size = browser.get_window_size()
        self.browser = browser
        self.camera = Camera(
            'demo.ogv',
            xPos=window_pos.get('x'),
            yPos=window_pos.get('y'),
            height=window_size.get('height'),
            width=window_size.get('width')
        )

    def __enter__(self):
        cameraman = Thread(target=self.camera.start_recording, args=())
        cameraman.start()

    def __exit__(self, type, value, traceback):
        self.camera.stop_recording()


class Scene(object):

    def __init__(self, script, narrator):
        self.script = script
        self.narrator = narrator

    def __enter__(self):
        narration = Thread(target=self.narrator.say, args=(self.script,))
        narration.start()

    def __exit__(self, type, value, traceback):
        pass

