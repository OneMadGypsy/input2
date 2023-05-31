import sys, re, operator
from pynput import keyboard

BACKSPACE = 8
ENTER     = 13
L_ARROW   = 37
R_ARROW   = 39

ALL       = tuple((9, *range(32, 127)))
ALL_AE    = (9,32)                     
ALL_TE    = tuple((46, *range(48,58))) 

NPVK      = range(96,106)
NPVK_OFS  = 48
DCVK      = 110
DCVK_OFS  = 64


class __:
    @property
    def caret(self) -> int:
        return self._ct
        
    @property
    def input(self) -> list[str]:
        return self._in[:]
        
    @property
    def output(self) -> str: 
        return "".join(self._in)
        
    @property
    def _x(self) -> list[str]: 
        return (self._in or [None]*(self._ct+1))
        
    def __init__(self):
        self._in = []
        self._ct = 0
    
    def _i(self, func:callable, i:int=0) -> int:
        return (-1, self._ct+i)[func(self._ct,len(self._in))]
    
    def update(self, data:list[str]) -> None:
        self._in = data
        
    def char(self, d:int) -> str:
        c = self._x[self._i(operator.lt)]
        self._ct += d
        return c
        
    def remchar(self) -> str:
        c = self._x.pop(self._i(operator.le, -1))
        self._ct -= 1 
        return c


def input2(prompt:str='', fmt:callable=None, expr:str=None, flags:int=0, req:str=None) -> str:
    fmt   = fmt or (lambda c: c)
    match = re.compile(fr'{expr or r"."}|[\b\n]$', flags).match
    req   = (lambda _: True) if not req else re.compile(fr'{req}', flags).match

    d = __()
    P = len(prompt)
    
    def write(m:str) -> None:
        sys.stdout.write(m)
        sys.stdout.flush()

    def emulator(key) -> bool:
        try:
            i  = ord(key.char)
            ok = i in ALL
        except AttributeError:
            i  = key.value.vk 
            ok = i in ALL_AE + (BACKSPACE, ENTER)
        except TypeError:
            i  = key.vk 
            i -= NPVK_OFS * (i in NPVK) + DCVK_OFS * (i == DCVK)
            ok = i in ALL_TE
            
        if ok:
            c, e = chr(i), False
    
            if t := (i in ALL): 
                L = len((tmp := d.input))
                
                if d.caret < L: tmp[d.caret] = c
                else          : tmp.append(c)
                    
                if not match(tmp := fmt(''.join(tmp))): 
                    return True
                
                d.update(list(tmp))
    
            elif i==BACKSPACE:
                if d.remchar():
                    n     = sum(3*(c=='\t') for c in d.output)+1
                    L     = len(d.input)
                    blank = chr(0)*(P+L+n)
                    caret = chr(8)*(L-d.caret)
                    write(f'\r{blank}\r{prompt}{d.output}{caret}')
                    
                return True
                
            elif (e := (i==ENTER)) and not req(d.output):
                return True
    
            write(('\n', d.char(1) or '')[(not e) & t])
            
            return not e
            
        elif i in (L_ARROW, R_ARROW):
            r = i==R_ARROW
            if -r < d.caret <= (len(d.input)-r):
                write(('\b', d.char((-1,1)[r]) or '')[r])
                
        return True
        
    write(prompt)
        
    with keyboard.Listener(on_press=emulator) as listener:
        listener.join()
     
    return d.output


if __name__ == '__main__':
    strawman = input2('Full Name: ', str.upper, r'^[a-z ]+$', re.I, r'^[a-z]{2,} [a-z]{2,}$')
    print(strawman)
