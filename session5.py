"""
Module docstring:

To have a generalized time_it function (like Python's timeit)
that would enable to take in any function that has to be timed,
with proper arguments.

To also have other utility functions that would enable to test the `time_it` function.
Tests in `test_session5.py` file

Cyclomatic Complexity result:
----------------------------------------------------------------------
reference for CC:
CC score    Rank    Risk
-------    ------   -----
1 - 5       A       low - simple block
6 - 10      B       low - well structured and stable block
11 - 20     C       moderate - slightly complex block
21 - 30     D       more than moderate - more complex block
31 - 40     E       high - complex block, alarming
41+         F       very high - error-prone, unstable block

results ---->
    F 185:0 temp_converter - C (12)
    F 233:0 speed_converter - B (10)
    F 113:0 squared_power_list - B (9)
    F 153:0 polygon_area - B (8)
    F 66:0 time_it - B (6)

    5 blocks (classes, functions, methods) analyzed.
    Average complexity: B (9.0)


Raw metrics:
----------------------------------------------------------------------
for reference:
LOC: the total number of lines of code
LLOC: the number of logical lines of code
SLOC: the number of source lines of code - not necessarily the LLOC
comments: the number of Python single comment lines
multi: the number of lines representing multi-line strings
blank: the number of blank lines (or whitespace-only ones)

RAW metric values ---->
    LOC: 227
    LLOC: 88
    SLOC: 81
    Comments: 0
    Single comments: 0
    Multi: 110
    Blank: 36

======================================================================
"""

import math
import time
import types
from typing import Union


def time_it(fn: types.FunctionType, *args, repetitions: int = 1, **kwargs) -> Union[float, Exception]:
    """
    This is a generalized function to call any function
    user specified number of times and return the average
    time taken for calls

    Parameters
    ----------
    fn : The actual function to TIME, with logs, checks performed before usage, type: function & callable, NOTE: positional argument
    args : Arbitrary number of positional-only arguments for the `fn`
    repetitions: type: int, default = 1: The number of time this timer utility will run the code to call and test `fn`
    kwargs : Arbitrary keyword-only arguments for param: fn to be used
    -------
    Returns -> Average time, in seconds, taken for calling `fn` for `repetitions`, type: float
    """

    if not (isinstance(fn, (types.FunctionType, types.BuiltinFunctionType)) and hasattr(fn, '__call__')):
        return TypeError("😠 Hey dude! \
            You are supposed to pass a function to time for `fn`!")
    if repetitions < 0:
        return TypeError("Seriously man! 🙄 Do I need to tell you that repetitions would have to be positive")
    start = time.perf_counter()
    for _ in range(repetitions):
        result = fn(*args, **kwargs)
        print(f"Result for {fn}, count: {_} is: {result}")
    end = time.perf_counter()
    return (end - start) / repetitions if repetitions else 0


def squared_power_list(number: int, *args, start: int = 0, end: int = 5, **kwargs) -> Union[list, Exception]:
    """
    Creates a list by raising numbers to the given values of power,
    from start to end
    Parameters
    ----------
    number : type: int, the number/base which is raised to powers and added, must be less than 10
    start : the start value, number**start
    end : the end range value, number**end
    -------
    Returns -> a list with elements [number**start, number**(start+1) to number**end]
    -------
    -------
    """
    if not isinstance(number, int):
        raise TypeError("Hey, Only integer type arguments are allowed ")
    if start < 0 or end < 0 or (end < start):
        raise ValueError("Value of start or end can't be negative and Value of start should be less than end")
    if number > 10:
        raise ValueError("Value of number should be less than 10")
    if args:
        raise TypeError("sqaured_power_list takes maximum 1 positional arguments")
    if kwargs:
        raise TypeError("sqaured_power_list takes maximum 2 keyword/named arguments")
    return [number ** x for x in range(start, end)]


def polygon_area(length: int, *args, sides: int, **kwargs) -> Union[float, Exception]:
    """
    Calculates the area of a regular polygon with number of sides between 3 to 6 range (inclusive)
    Parameters
    ----------
    length : positive integer value to use as length of each side
    sides : number of sides to use, must be between 3 to 6 range
    -------
    Returns -> area of polygon using the given length and sides, type: float
    -------
    -------
    """
    if not (isinstance(length, int) and isinstance(sides, int)):
        raise TypeError("Only integer type arguments are allowed")
    if length < 1:
        raise ValueError("😤 Again !! 'length' should be positive")
    if sides < 3 or sides > 6:
        raise ValueError("Kindly check value of sides given, must be in range 3,6 inclusive")
    if args:
        raise TypeError("polygon_area function takes maximum 1 positional arguments, more provided 😒")
    if kwargs:
        raise TypeError("polygon_area function take maximum 1 keyword/named arguments, more provided 🙄")
    return (sides * length ** 2) / (4 * math.tan(math.pi / sides))


def temp_converter(temp, *args, temp_given_in: str = 'f', **kwargs) -> Union[float, Exception]:
    """
    Converts temperature from celsius 'c' to fahrenheit 'f' or fahrenheit to celsius
    Parameters
    ----------
    temp : type: float/int: the value to be converted
    temp_given_in : type: str: the flag to tell which is the source scale (either f or c)
    args : to scoop other additional arbitrary positional arguments
    kwargs : to scoop other additional arbitrary keyword-only arguments
    -------
    Returns -> converted value(s) for temperature in a list
    -------
    -------
    """
    if not isinstance(temp, (int, float)):
        raise TypeError("Only float/int type arguments are allowed")

    if not isinstance(temp_given_in, str):
        raise TypeError("Character string expected")

    if temp_given_in.lower() not in ['c', 'f']:
        raise ValueError("Only f or c is allowed")

    if args:
        raise TypeError("temp_converter function takes maximum 1 positional arguments, more provided")
    if kwargs:
        raise TypeError("temp_converter function take maximum 1 keyword/named arguments, more provided")

    if temp_given_in.lower() == 'c' and temp < -273.15:
        raise ValueError("Temperature can't go below -273.15 celsius = 0 Kelvin")
    if temp_given_in.lower() == 'f' and temp < -459.67:
        raise ValueError("Temperature can't go below -459.67 fahrenheit = 0 Kelvin")

    if temp_given_in.lower() == 'c':
        return round(temp * (9 / 5) + 32, 4)
    if temp_given_in.lower() == 'f':
        return round((temp - 32) * 5 / 9, 4)


def speed_converter(speed, *args, dist: str = 'km', time: str = 'min', **kwargs) -> Union[float, Exception]:
    """
    Converts speed from kmph (provided by user as input) to different units,
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day

    Parameters
    ----------
    speed : type: float/int: the speed value to use for conversion

    dist : type: str: the distance metric type to use for conversion

    time : type: str: the time metric to use for conversion

    args : to scoop other additional arbitrary positional arguments

    kwargs : to scoop other additional arbitrary keyword-only arguments
    -------
    Returns -> converted value(s) for speed(s) provided
    -------
    -------
    """
    if not isinstance(speed, (int, float)):
        raise TypeError("😑 Speed can be int or float type only")
    if not isinstance(dist, str):
        raise TypeError(" Character string expected for distance unit")
    if not isinstance(time, str):
        raise TypeError("Character string expected for time unit")

    if args:
        raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided")
    if kwargs:
        raise TypeError("speed_converter function take maximum 2 keyword/named arguments, more provided")

    if speed < 0 or speed >= 300001:
        raise ValueError("️ Speed can't be negative and Speed can't be greater than speed of light!")

    dist, time = dist.lower(), time.lower()
    if dist not in {'km', 'm', 'ft', 'yrd'}:
        raise ValueError(" Incorrect unit of distance. Only km/m/ft/yrd allowed 🤷🏻‍️")

    if time not in {'ms', 's', 'min', 'hr', 'day'}:
        raise ValueError("😐 Incorrect unit of Time. Only ms/s/min/hr/day allowed")

    km_to = {'m': 1000, 'ft': 3280.8375, 'yrd': 1093.609}
    hr_to = {'ms': 3600000, 's': 3600, 'min': 60, 'day': 1 / 24}
    value = speed * km_to.get(dist, 1) / hr_to.get(time, 1)
    return float(round(value))
