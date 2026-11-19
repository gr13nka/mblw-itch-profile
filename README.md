# mblw itch profile

The custom CSS of [mblw.itch.io](https://mblw.itch.io): a Nintendo DS home menu over itch's grid layout.

itch's Custom CSS field holds about 5 KB, so it only imports the built file:

```css
@import url(https://cdn.jsdelivr.net/gh/gr13nka/mblw-itch-profile@<commit>/profile.min.css);
```

Edit `profile.css`, run `python3 build.py art`, commit, and put the new commit hash in that line.
