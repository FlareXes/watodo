# Watodo
Very Minimal Todo Script With No Garbage - Which Suckless So, Just Do It Now. `Watodo` Tells What To Do? On Terminal.

# Usage
Add A Task
```bash
python watodo.py a [Text Here]
```
Mark A Task Complete
```bash
python watodo.py c [No. Of Task]
```
Example, Mask Task 2 As Complete
```bash
python watodo.py c 2
```
To List In-Progress Tasks Just Do
```bash
python watodo.py
```
List All Tasks
```bash
python watodo.py h
```

# Arguments
Args | Description |
---|---
a | Add a todo
c | Mark todo as complete
h | Show history
reset | Forget all todos including history

# Requirements
- rich
```bash
pip install rich
```

# Installation
### Linux / MacOS
```bash
git clone https://github.com/FlareXes/watodo.git

cd watodo

chmod +x setup.sh watodo 

./setup.sh
```
Now you can remove the repo and also don't need to type `python watodo.py`. Just do `watodo` anywhere in terminal.

Example
```bash
watodo a update github repo
```

```bash
watodo c 3
```

# Uninstall
1. Remove The ***watodo.py*** Script Where You Stored It
2. Then, Just Remove The Database Directory At ***~/.config/watodo***

    ```bash
    rm -rf ~/.config/watodo /opt/watodo /usr/local/bin/watodo
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
