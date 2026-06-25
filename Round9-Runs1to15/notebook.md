# About Interpreter.py

### Timer class
- `click` is set to 0 to signal `initial` needs a value, and 1 when `final` needs a value
- `initial` is the time at first elapse, preset to 0
- `final` is the time at last elapse, preset to 0

`elapse` is the sole function, called once to assign `initial` value and twice to assign `final` value. A the second call, the difference is returned (to 3 d.p)

### Interpreter class
- `filepath` is a string referring to the `.dat` file analyzed
- `runtime` is defined by a `Timer` instance later on
- `header` is a list of data column
- `data` is the list of decimal values attributed to each data column

`parse` is a private function, called to attempt restructuring of `.dat` filelines into a dictionary of data columns. This is timed to evaluate efficiency.

`summary` is a public function, calling `parse` and reporting the runtime for the function.

`__main__`: Intended use is to go through individual `.dat` files as efficiently as possible