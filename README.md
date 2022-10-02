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
