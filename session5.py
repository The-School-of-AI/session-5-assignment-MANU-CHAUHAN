"""
Module docstring:
    To have a generalized time_it function (like Python's timeit)
    that would enable to take in any function that has to be timed, with proper arguments obviously.

    To also have other utility functions that would also enable to test the `time_it` function.

    Last Pylint run result:
    ----------------------------------------------------------------------
        Your code has been rated at 8.68/10 (previous run: 8.43/10, +0.25)


    Cyclomatic Complexity result:
    ----------------------------------------------------------------------
    (reference for CC):
    CC score	Rank	Risk
    -------    ------   -----
    1 - 5	    A	    low - simple block
    6 - 10	    B	    low - well structured and stable block
    11 - 20	    C	    moderate - slightly complex block
    21 - 30	    D	    more than moderate - more complex block
    31 - 40	    E	    high - complex block, alarming
    41+ 	    F	    very high - error-prone, unstable block

    ---->
    F 64:0 squared_power_list - B (7)
    F 123:0 temp_converter - B (7)
    F 20:0 time_it - B (6)
    F 158:0 speed_converter - B (6)
    F 98:0 polygon_area - A (5)

    5 blocks (classes, functions, methods) analyzed.
    Average complexity: B (6.2)


    Raw metrics:
    ----------------------------------------------------------------------
    (reference):
    LOC: the total number of lines of code
    LLOC: the number of logical lines of code
    SLOC: the number of source lines of code - not necessarily corresponding to the LLOC
    comments: the number of Python comment lines (i.e. only single-line comments #)
    multi: the number of lines representing multi-line strings
    blank: the number of blank lines (or whitespace-only ones)

    ---->
    LOC: 256
    LLOC: 61
    SLOC: 67
    Comments: 3
    Single comments: 2
    Multi: 122
    Blank: 65


======================================================================
"""

import math
import time
import types
import traceback
from typing import Union


def time_it(fn: types.FunctionType, *args, repetitions: int = 1,
            **kwargs) -> Union[float, Exception]:
    """
    This is a generalized function to call any function
    user specified number of times and return the average
    time taken for calls

    Parameters
    ----------
    fn : The actual function to TIME, with logs, checks performed before usage,
        type: function & callable,
        NOTE: positional argument

    args : Arbitrary number of positional-only arguments for the `fn` to be used

    repetitions: type: int, default = 1: The number of time this timer utility will
                run the code to call and test `fn`,
                checks performed before usage for positive value, NOTE: a keyword-only argument

    kwargs : Arbitrary keyword-only arguments for param: fn to be used

    -------
    Returns -> Average time, in seconds, taken for calling `fn` for `repetitions`, type: float
    -------
    -------
    """
    if not (isinstance(fn, types.FunctionType) and hasattr(fn, ' __call__')):
        return TypeError("😠 Hey dude! You are supposed to pass a function to time for `fn`!")
    if repetitions <= 0:
        return TypeError("Seriously man!"
                         " 🙄  Do I need to tell you that `repetitions` would have to be > 0 !")
    try:

        start = time.perf_counter()
        for _ in range(repetitions):
            fn(*args, **kwargs)
        end = time.perf_counter()
        return round((end - start) / repetitions, 5)

    except Exception:
        # print traceback in case of any Exception raised by :param fn
        print(traceback.print_exc())


def squared_power_list(number: int, *args, start: int = 0, end: int = 5, **kwargs) \
        -> Union[list, Exception]:
    """
    Creates a list by raising numbers to the given values of power from start to end

    Parameters
    ----------
    number : type: int, the number/base which is raised to powers and added in list,
            if only one number is provided use it for every list element,
            otherwise if *args hold the numbers use those

    args : to scoop other additional arbitrary positional arguments

    start : the start value, number ^ start

    end : the end range value, number ^ end

    kwargs : to scoop other additional arbitrary keyword-only arguments

    -------
    Returns -> a list with elements [number ^ start, number ^ (start+1), ..., number ^ end]
    -------
    -------
    """
    if start < 0 or end < 0 or (end < start):
        raise ValueError("What!!! 😑 'start' and 'end' values cannot be -ve."
                         " And 'end' must be > 'start'")

    nums = [number] + list(args)

    results = [[number ** x for x in range(start, end + 1)] for number in nums]
    return results[0] if len(results) == 1 else results


def polygon_area(length: int, *args, sides: int = 3, **kwargs) -> Union[list, Exception]:
    """
    Calculates the area of a regular polygon with number of sides between [3, 6] range (inclusive)

    Parameters
    ----------
    length : positive integer value to use as length of each side
    sides : number of sides to use, must be between [3, 6] range

    -------
    Returns -> area of polygon using the given length and sides, type: float
    -------
    -------
    """
    if not (length > 0 or (3 <= sides <= 6)):
        raise ValueError("😤 Again !! 'length' should be positive and"
                         " sides should be within closed range [3,6]")

    lengths = [length] + list(args)  # to use dynamic number of positional length values

    # return list containing one or n number of polygon_areas corresponding to each length
    result = [(sides * length ** 2) / (4 * math.tan(math.pi / sides)) for length in lengths]
    return result[0] if len(result) == 1 else result


def temp_converter(temp, *args, temp_given_in: str = 'f', **kwargs) -> Union[list, Exception]:
    """
    Converts temperature from celsius 'c' to fahrenheit 'f' or fahrenheit to celsius

    Parameters
    ----------
    temp : type: float/int: the value to be converted

    temp_given_in : type: str: the flag to tell which is the source scale (either f or c)

    args : to scoop other additional arbitrary positional arguments,
            use these if these are same type as temp and convert all

    kwargs : to scoop other additional arbitrary keyword-only arguments

    -------
    Returns -> converted value(s) for temperature in a list
    -------
    -------
    """

    if temp_given_in.lower() not in ['c', 'f']:
        raise TypeError("😒, No other worldly temperature conversion scales,"
                        " not yet (yeah... not even Kelvin)")

    temps = [temp] + list(args)

    if temp_given_in.lower() == 'c':
        result = [temp * (9 / 5) + 32 for temp in temps]
    if temp_given_in.lower() == 'f':
        result = [(temp - 32) * 5 / 9 for temp in temps]

    return result[0] if len(result) == 1 else result


def speed_converter(speed: float, *args, dist_type: str = 'km',
                    time_type: str = 'min', **kwargs) -> Union[list, Exception]:
    """
    Converts speed from kmph (provided by user as input) to different units,
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day

    Parameters
    ----------
    speed : type: float: the speed value to use for conversion

    dist_type : type: str: the distance metric type to use for conversion

    time_type : type: str: the time metric to use for conversion

    args : to scoop other additional arbitrary positional arguments,
            use these if these for same logic as speed if given

    kwargs : to scoop other additional arbitrary keyword-only arguments

    -------
    Returns -> converted value(s) for speed(s) provided
    -------
    -------
    """

    if speed < 0:
        raise ValueError("🤦🏻‍♂️ What is wrong with you today? Why are you obsessed with -ve values?"
                         " Are you a hard core pessimist? Is it your nihilistic view towards life?"
                         "Or is it existentialism? I recommend stoic texts,"
                         " perhaps that would help.")

    if dist_type not in {'km', 'm', 'ft', 'yrd'}:
        raise TypeError(
            "Woah.. wait.. are you from an alternative parallel universe"
            " where you have other system and scales? "
            " given 'dist' type is not among the implemented types ('km', 'm', 'ft', 'yrd') 🤷🏻‍♂️")

    if time_type not in {'ms', 's', 'm', 'hr', 'day'}:
        raise TypeError(
            " 😐 given 'time' type is not among the implemented types ('ms', 's', 'm', 'hr', 'day')")

    def km_to(convert_to: str):
        return {'m': 1000, 'ft': 3280.84, 'yrd': 1093.61}.get(convert_to, 1)

    def hr_to(convert_to: str):
        return {'ms': 3.6e6, 's': 3600, 'm': 60, 'day': 1 / 24}.get(convert_to, 1)

    speeds = [speed] + list(args)

    results = [speed * km_to(dist_type) / hr_to(time_type) for speed in speeds]

    return results[0] if len(results) == 1 else results
