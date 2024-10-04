# Obfuscated Python "methods" 🎭
> Oct 4, 2024, Reference: talk given by Jack Diedrich at PyCon US 2012; https://pyvideo.org/pycon-us-2012/stop-writing-classes.html

### Where it all started!

When I have started with Python, I happened to come across this deep quote about Python programming language,
> Everything is a "first class" object in Python, Mark Lutz, Python: Powerful Object oriented programming

It sort of triggered me to write everything as a class in my beginning days. In the beginning days, I felt like an imposter if I could not write any logic into a class 😵. Which eventually faded off, as it is supposed to. 

Are we getting into "Logic XYZ has to be a class or a method?" debate. No ❌, we are not getting into that rabbit hole 🌀 now, as it is a very subjective opinion. But we can call out when a method has been obfuscated as a class 😷. Trust me, there are markers, aka indicators.

### Let's get the party started 🎉

We shall discuss and bisect three different examples, where `class` was not necessary and rewrite to `methods`. 

#### Example 1: A class with two methods
_Problem_: Convert Celsius (°C) to Fahrenheit (°F). 
Let's write ~~class~~ solution!
```py title="c_to_f.py"
class TemperatureConverter:
    def __init__(self, celsius: int) -> None:
        self.celsius = celsius
    
    def _to_fahrenheit(self) -> float:
        return (self.celsius * 9/5) + 32

temp = TemperatureConverter(25)
fahrenheit = temp._to_fahrenheit()
print(f"25 °C is equal to {fahrenheit} °F")
```

There are two major indicators in the above example, which says it is not a `class` material. 
1. The class have just single functionality 🤦
2. Among two class methods, one is `__init__` 🤯

The developer could have thought of extending the class to convert to more metrics. But, that is not the problem statement asks for. Over preparedness ends up with bloated code base with unwanted LOC 📈. 

This can be simply re-written as the method below,
```py title="c_to_f_method.py"

def convert_to_fahrenheit(celsius: int) -> float:
    return (self.celsius * 9/5) + 32

print(f"25 °C is equal to {convert_to_fahrenheit(25)} °F")
```

Just, keep it simple, stupid [(K.I.S.S)](https://www.interaction-design.org/literature/topics/keep-it-simple-stupid)!

#### Example 2: The overthought class

_Problem_: Write text processor for counting words, counting characters and convert all letters to capital. 

Ah! Sounds like a need for class 🏃‍♂️, Isn't it? Below is the class implementation for the solution, looks good? 

```py title="text_processor.py"
class TextProcessor:
    def __init__(self, text: str) -> None:
        self.text = text
    
    def word_count(self) -> str:
        return len(self.text.split())
    
    def char_count(self) -> str:
        return len(self.text)
    
    def to_uppercase(self) -> str:
        return self.text.upper()

processor = TextProcessor("hello, world!")
print(f"Word count: {processor.word_count()}")
print(f"Character count: {processor.char_count()}")
print(f"Uppercase: {processor.to_uppercase()}")
```

No, definitely no. This is a bad implementation for few reasons. 
1. Additional overhead for instantiating an object. Like, seriously? 
2. There is no need to maintain state of the input. It is exclusive across methods. 
3. No shared functionalities between the methods as well. 

So, how this could have been implemented? 🤔
I would prefer having a separate module where all my text processing functions/methods are available to be shared across the code base. So, create a module and add the functions. 

```py title="text-processing-functions.py"
def get_word_count(text: str) -> int:
    return len(text.split())

def get_character_count(text: str) -> int:
    return len(text)

def capitalize_text(text: str) -> str:
    return text.to_uppercase()

text = "hello, world!"
print(f"Word count: {get_word_count(text)}")
print(f"Character count: {get_character_count(text)}")
print(f"Uppercase: {capitalize_text(text)}")
```

This is the representation of first S in [SOLID](https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/). A method holds only single responsibility. Functions are enough to deal with stateless input data. 

To explain what does "state of data" means, consider `bank_balance` as an attribute in `BankAccount` class. It is susceptible to change when passed through `deposit` or `withdraw` methods.

### Conclusion

Class is great! But when you solve a problem with a class which can be solved by a mere function, then you are overusing it. 
> Simple is better than complex; Readability counts, Zen of Python

