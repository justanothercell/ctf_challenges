# Solution

```py
import json
s = "import json\ns = $\nc = s.replace(\"$\", json.dumps(s), 1)\nprint(c)"
c = s.replace("$", json.dumps(s), 1)
print(c)
```
