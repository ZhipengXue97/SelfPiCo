# Extracted from https://stackoverflow.com/questions/375427/a-non-blocking-read-on-a-subprocess-pipe-in-python
import io
from subprocess import PIPE, Popen

p = Popen(['myprogram.exe'], stdout=PIPE)

SLEEP_DELAY = 0.001

# Create an io.BufferedReader on the file descriptor for stdout
with io.open(p.stdout.fileno(), 'rb', closefd=False) as buffer:
  while p.poll() == None:
      time.sleep(SLEEP_DELAY)
      while '\n' in bufferedStdout.peek(bufferedStdout.buffer_size):
          line = buffer.readline()
          # do stuff with the line

  # Handle any remaining output after the process has ended
  while buffer.peek():
    line = buffer.readline()
    # do stuff with the line

