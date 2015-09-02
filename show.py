#!/usr/bin/env python
import os
import re
import sys
import signal
import subprocess
filename = sys.argv[1]
root, ext = os.path.splitext(filename)
lines = open(root + '.ipynb').read()
regex = re.compile(r'<a.*?>.*?<\/a>')
lines = regex.sub('', lines)
slides = root + '_slides.ipynb'
with open(slides, 'w') as fh:
    fh.write(lines)
reveal = '--reveal-prefix "http://cdn.jsdelivr.net/reveal.js/2.6.2"'
cmd = 'ipython nbconvert --to slides --post serve {0} {1}'.format(reveal, slides)
try:
    proc = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid)
except KeyboardInterrupt:
    os.killpg(proc.pid, signal.SIGTERM)