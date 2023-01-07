# Watodo
Very Minimal Todo Script With No Garbage - Which Suckless So, Just Do It Now. `Watodo` Tells What To Do? On Terminal.

# Installation
### Linux / MacOS
```bash
git clone https://github.com/FlareXes/watodo.git && cd watodo

chmod +x setup && ./setup
```

### Windows
Only `watodo.py` file is required
```
git clone https://github.com/FlareXes/watodo.git

python watodo.py
```

# Usage

## Arguments

Args | Description |
---|---
a | Add a todo
c | Mark todo as complete
h | Show history
reset | Forget all todos including history
help | Show help menu


## Examples

To add a todo
```bash
watodo a [Todo Here]
```
To mark a todo as complete
```bash
watodo c [Todo Sno]
```
Example, Mask Task 2 As Complete
```bash
watodo c 2
```
To List Current Todos
```bash
watodo
```
To List All Tasks
```bash
watodo h
```

# Uninstall
```bash
sudo rm -rf ~/.local/share/watodo /opt/watodo /usr/local/bin/watodo
```

# License

MIT License

Copyright (c) 2022 FlareXes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
