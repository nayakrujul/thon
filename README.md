# Thon

A very concise golfing language

## Installation

#### From PyPI

```zsh
$ pip install thon
```

## Links to this repository

#### Plain URL

```
https://github.com/nayakrujul/thon
```

#### HTML

```html
<a href="https://github.com/nayakrujul/thon">Thon</a>
```

#### Markdown

```
[Thon](https://github.com/nayakrujul/thon)
```

## Running code

### Simple

Use the `thon` command in the terminal, followed by your code.

```zsh
$ thon "NS"
```

### Flags

The `thon` command takes in some flags. Here they are. An example usage is `thon "S" -il`.

#### `-el`

* Without the `-el` flag, the element at the top of the stack is implicitly output at the end of the program.
* Just using `-el` removes the implicit output
* Specifying a number, `n`, after `-el`, e.g. `-el 3`, means `n` elements from the top of the stack will be output at the end of the program.

#### `-hw`

Implicitly push `"Hello, world!"` at the start of the program.

#### `-ii`

Implicitly input one integer at the start of the program.

#### `-il`

Implicitly input a list of integers, separated by spaces, at the start of the program.

#### `-si`

Implicitly input one string at the start of the program.

#### `-sl`

Implicitly input a list of strings, separated by spaces, at the start of the program.

#### `-js`

Join the elements that are implicitly output at the end by a space.

#### `-jc`

Join the elements that are implicitly output at the end by a comma.

#### `-jn`

Join the elements that are implicitly output at the end by a new line.

## Tutorial

### Introduction

Thon, like many other golfing languages, is stack-based. This means that whenever you perform an operation, the result is pushed to the top of the *stack*, a list of every variable that has been used.

Unlike many other golfing languages, Thon does not use special symbols. Every character in Thon is in the printable ASCII character set, meaning you can find it on a standard keyboard.

### Arithmetic

#### Numbers

To push a number to the top of the stack, just write it. These are all valid numbers:

* `1` = integer, 1
* `123` = integer, 123
* `1.23` = float, 1.23
* `1.` = float, 1.0
* `.1` = float, 0.1

#### Operators

Thon has these operators for numbers:

* `+`: addition
* `-`: subtraction
* `*`: multiplication
* `/`: division
* `^`: exponentiation

In Thon, the numbers come *first*, and the operator is at the end. For example, to add `1` and `2`, use:

```
1 2+
```

### Strings

A string in Thon starts and ends with a double quote (`"`)

```
"Hello, world!"
```

However, if the closing quote is at the very end of the program, you can leave it out. It will be autocompleted by the interpreter:

```
"Hello, world!
```

### Lists

To create an empty list in Thon, use `L`. Then, to append to it, use `A`:

```
L1A2A3A
```

(creates a list, `[1, 2, 3]`)

To remove the first instance of an element from a list, use `R`:

```
L1A23A1R
```

(creates a list, `[1, 2, 3]`, then removes 1 from it, leaving the list as `[2, 3]`)

To get the sum of a list, use `S`:

```
L1A2A3AS
```

(creates a list, `[1, 2, 3]`, then sums it, giving an output of `6`)

To get the product of a list, use `P`:

```
L1A2A4AP
```

(creates a list, `[1, 2, 4]`, then gets its product, giving an output of `8`)

### Indexing

Lists and strings can be indexed. In Thon, these keys are used for indexing:

* `q` = 1<sup>st</sup> element
* `w` = 2<sup>nd</sup> element
* `e` = 3<sup>rd</sup> element
* `r` = 4<sup>th</sup> element
* `t` = 5<sup>th</sup> element
* `y` = 5<sup>th</sup> last element
* `u` = 4<sup>th</sup> last element
* `i` = 3<sup>rd</sup> last element
* `o` = 2<sup>nd</sup> last element
* `p` = last element

For example:

```
"Hello, world!"i
```

This outputs `'l'`, because `l` is the 3<sup>rd</sup> last element of the string

### Inputs

To input an integer, use `n`.

To input a list of integers, separated by spaces, use `N`.

To input a string, use `c`.

To input a list of strings, separated by spaces, use `C`.

### Loops

The Thon equivalent of a `for` loop is `{` `}`:

```
L"Hello"{A}
```

Loops through the string `"Hello"`, and appends each character to the empty list declared at the start. Output: `['H', 'e', 'l', 'l', 'o']`

### Base conversion

To convert an integer to any base (up to 64), use `B`, specifying the number, and then the base.

```
18 2B
```

Output: `'10010'` (18 in binary)

To convert a number in any base to decimal (base-10), use `D`.

```
"10010"2D
```

Output: `18`

### Conditionals

Thon has a ternary conditional operator which is similar to many other programming languages.

It follows the form: `condition ? if_true : if_false`

For example:

```
n?"Yes":"No"
```

If the user input is *truthy*, i.e. not 0, it will output `"Yes"`. Otherwise, it will output `"No"`.

You can use the operators `>`, `<`, and `=` with numbers. They work just like arithmatic operators:

```
n5>?"Yes":"No"
```

This will output `"Yes"` if the user input was greater than 5, and `"No"` if it wasn't.

## Example programs

Here are some example programs in Thon, compared with their Python equivalents.

### Output "Hello, world!"

#### Python

```python
print("Hello, world!")
```

#### Thon (no flags)

```
"Hello, world!
```

#### Thon `-hw`

```
```

### Sum the numbers which are input by the user

#### Python

```python
print(sum(map(int, input().split())))
```

#### Thon (no flags)

```
NS
```

#### Thon `-il`

```
S
```

### Input a hexadecimal number and convert to binary

#### Python

```python
print(bin(int(input(), 16))[2:])
```

#### Thon (no flags)

```
c16D2B
```

#### Thon `-si`

```
16D2B
```
