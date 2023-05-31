# input2
python `input` emulator with added functionality

-------

## Arguments
|args|description|
|-|-|
|prompt | the user prompt|
|fmt    | `str.upper`, `str.lower`, `str.title`, etc..|
|expr   | compiled and used to match `fmt` return data|
|flags  | `re.compile` flags|
|req    | compiled and used to match final data|

--------

## Details

* All arguments are optional. When an argumanet is omitted it is defaulted to a "does nothing" value.
* Formatting is applied before the input is matched. 
* backspace, Left, Right and the full numlocked Numpad are supported

-------

## Usage
```python3
from scratch import input2

full_name = input2('Full Name', self.title, r'^[a-z ]+$', re.I, r'^[a-z]{2,} [a-z]{2,}$')
```
