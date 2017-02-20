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
import signal
import subprocess

# TODO (rbrady): add camera based on ffmpeg


class CameraBase(object):

    def __init__(self):
        pass

    def start_recording(self):
        pass

    def pause_recording(self):
        pass

    def unpause_recording(self):
        pass

    def stop_recording(self):
        pass


class Camera(CameraBase):
    def __init__(self, output_file, xPos=None, yPos=None, height=None,
                 width=None):
        self.output_file = output_file
        self.recording = False
        self.stderr = None
        self.stdout = None

        recording_args = ['recordmydesktop']
        if xPos:
            recording_args.append("-x")
            recording_args.append(str(xPos))
        if yPos:
            recording_args.append("-y")
            recording_args.append(str(yPos))
        if height:
            recording_args.append("-height")
            recording_args.append(str(height))
        if width:
            recording_args.append("-width")
            recording_args.append(str(width))

        recording_args.append("-o")
        recording_args.append(self.output_file)

        self.process = subprocess.Popen(
            recording_args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

    def start_recording(self):
        self.stdout, self.stderr = self.process.communicate()
        if self.stderr == '':
            self.recording = True

    def toggle_pause(self):
        self.process.send_signal(signal.SIGUSR1)
        return self.process.communicate()

    def pause_recording(self):
        stdout, stderr = self.toggle_pause()

    def unpause_recording(self):
        stdout, stderr = self.toggle_pause()

    def stop_recording(self):
        self.process.send_signal(signal.SIGINT)
        return self.process.communicate()

