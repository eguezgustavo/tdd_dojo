# Clean code python

Clean code does one thing well.
Write code that other people can maintain and use.

## Variables

### Meaningful Naming

The name of a variable should be a noun.

#### Use meaningful and pronounceable variable names

The name of the variable should reveal what we intend to do with the variable and it has to be pronounceable for humans:

Bad:

```py
import datetime


swdate = datetime.date.today().strftime("%y-%m-%d")

```

Good:

```py
import datetime


start_working_date = datetime.date.today().strftime("%y-%m-%d")

```

### Use searchable names

Single-letter names and numeric constants have a particular problem: they are not easy to locate across a body of text. A good rule for this is: The length of a variable name should be proportional to the size of the scope that contains it. So, if you have a 1-line loop,like in dict comprehension or list comprehension it is ok to use i as a variable.

Bad:
```py
h = get_worked_hours_per_month()
p = 10
result = h * p
```
Good:
```py
worked_hours_per_month = get_worked_hours_per_month()
pay_per_hour_in_usd = 10
salary_in_usd = worked_hours_per_month * pay_per_hour_in_usd

```

### Use the same vocabulary for the same type of variable

Bad:
```py
def get_user_info(): pass
def get_client_data(): pass
def get_person_record(): pass
def get_customer_profile(): pass
```
Good:
```py
def get_user(): pass
```

### Avoid mental mapping

Don’t force the reader of your code to translate what the variable means. Explicit is better than implicit.

Bad:
```py
t = ("Austin", "New York", "San Francisco")

for i in t:
    #do_stuff()
    #do_some_other_stuff()

    # Wait, what's `i` again?
    print(i)
```
Good:
```py
locations = ("Austin", "New York", "San Francisco")

for location in locations:
    #do_stuff()
    #do_some_other_stuff()
    # ...
    print(location)
```

### Don't add unneeded context

If your class/object name tells you something, don't repeat that in your variable name.

Bad:

```py
class Car:
    car_make: str
    car_model: str
    car_color: str
```

Good:

```py
class Car:
    make: str
    model: str
    color: str
```

### Avoid magic string

Magic strings are string values that are specified directly within application code that have an impact on the application’s behavior. Frequently, such strings will end up being duplicated within the system. So, bugs are introduced, when changes are made to some strings but not others.

Bad:

```py
if user_role == 'admin':
    # do something
```

Good:

```py
admin_role = 'admin'
if user_role == admin_role:
    # do something
```

## Functions

Functions should not be more than 20 lines, and functions only do one thing, but what is one thing? It is recommendable that the function does not have more than 3 arguments because it makes testing your function easier. Zero arguments is the ideal case. One or two arguments is ok, and three should be avoided. Anything more than that should be consolidated. Usually, if you have more than two arguments then your function is trying to do too much. In cases where it's not, most of the time a higher-level object will suffice as an argument.
### Meaningful Naming

Functions names should have a verb or verb phrases, because functions do things. For example, delete_page, render_page or load_data.
### Functions should say what they do

Bad:

```py
class Email:
    def handle(self) -> None:
        pass

message = Email()
# What is this? A handle for the message? Are we writing to a file now?
message.handle()
```

Good:

```py
class Email:
    def send(self) -> None:
        pass

message = Email()
# Clear and obvious
message.send()
```

### Avoid side effects

A side effect could be writing to a file, modifying some global variable, or accidentally wiring all your money to a stranger.

Now, you do need to have side effects in a program on occasion, for example write to a particular file. To do this, you should have one service that does it. One and only one.

Bad:

```py
fullname = "Ryan McDermott"

def split_into_first_and_last_name() -> None:
    global fullname
    fullname = fullname.split()

split_into_first_and_last_name()

print(fullname)
```

Good:

```py
from typing import List, AnyStr


def split_into_first_and_last_name(name: AnyStr) -> List[AnyStr]:
    return name.split()

fullname = "Ryan McDermott"
name, surname = split_into_first_and_last_name(fullname)

print(name, surname)
```

### Don't use booleans as parameters of a function

Try not to send boolean arguments to a functions, sending booleans to a function means that there will be an if statement, so it is better to write a function for the true and another for the false condition.

Bad:

```py
from typing import Text
from tempfile import gettempdir
from pathlib import Path


def create_file(name: Text, temp: bool) -> None:
    if temp:
        (Path(gettempdir()) / name).touch()
    else:
        Path(name).touch()
```

Good:
```py
from typing import Text
from tempfile import gettempdir
from pathlib import Path


def create_file(name: Text) -> None:
    Path(name).touch()


def create_temp_file(name: Text) -> None:
    (Path(gettempdir()) / name).touch()
```

### Functions should only be one level of abstraction

Every line of the functions should be at the same level of abstraction.

Bad:

```py
# type: ignore

def parse_better_js_alternative(code: str) -> None:
    regexes = [
        # ...
    ]

    statements = code.split('\n')
    tokens = []
    for regex in regexes:
        for statement in statements:
            pass

    ast = []
    for token in tokens:
        pass

    for node in ast:
        pass
```

Good:
```py
from typing import Tuple, List, Text, Dict


REGEXES: Tuple = (
   # ...
)


def parse_better_js_alternative(code: Text) -> None:
    tokens: List = tokenize(code)
    syntax_tree: List = parse(tokens)

    for node in syntax_tree:
        pass


def tokenize(code: Text) -> List:
    statements = code.split()
    tokens: List[Dict] = []
    for regex in REGEXES:
        for statement in statements:
            pass

    return tokens


def parse(tokens: List) -> List:
    syntax_tree: List[Dict] = []
    for token in tokens:
        pass

    return syntax_tree
```

Source:

[Clean Code - Uncle Bob](https://www.youtube.com/watch?v=7EmboKQH8lM&t=3608s)

[clean-code-javascript](https://github.com/ryanmcdermott/clean-code-javascript)
