# input2
python `input` emulator with added functionality

--------

## Details

* this module requires [pynput](https://pypi.org/project/pynput/)
* All arguments are optional. When an argumanet is omitted it is defaulted to a "does nothing" value.
* Formatting is applied before the input is matched against `expr`. 
* Backspace, Left, Right and the full numlocked Numpad are supported
* If used, `req` only performs a match if enter is pressed

-------

## Arguments
|args|description|
|-|-|
|prompt | the user prompt|
|fmt    | `str.upper`, `str.lower`, `str.title`, etc..|
|expr   | compiled and used to match `fmt` return data|
|flags  | `re.compile` flags|
|req    | compiled and used to match final data|

-------

## Usage
```python3
from scratch import input2

full_name = input2('Full Name: ', self.title, r'^[a-z ]+$', re.I, r'^[a-z]{2,} [a-z]{2,}$')
```

```python3
from scratch import input2

move = input2('What would you like to do? ', None, r'^[a-z]{,5}$', re.I, r'^(east|west|north|south|look)$')
```

--------

## Inspiraton

I answered [this question](https://stackoverflow.com/q/76352527/10292330) on stackoverflow, and decided to finish the gist that I started.
