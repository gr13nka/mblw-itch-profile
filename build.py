"""Inlines the sprites from the folder in argv[1] (art/) into profile.css, minifies it and writes profile.min.css;
prints its length. Usage: python3 build.py art"""
import base64
import re
import sys
from pathlib import Path

here = Path(__file__).parent
art = Path(sys.argv[1])
css = (here / 'profile.css').read_text()
for name, file in [('MOUSE', 'mouse.png'), ('CURSOR', 'cursor.png')]:
    css = css.replace(f'url({name})', 'url(data:image/png;base64,' + base64.b64encode((art / file).read_bytes()).decode() + ')')
css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
css = re.sub(r'\s+', ' ', css)
css = re.sub(r'\s*([{};:,>])\s*', r'\1', css)
css = css.replace(';}', '}').strip()
(here / 'profile.min.css').write_text(css)
print(len(css), 'chars')
