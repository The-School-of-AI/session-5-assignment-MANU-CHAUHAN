# S5


## Fun Python facts:
1)  In a survey conducted by the United Kingdom in 2015, Python overtook French to be one of the most popular languages that are taught in primary schools. The results came as a shock as 6 out of 10 parents wanted their children to learn Python instead of French.

2) type `import antigravity` in Python IDLE, make sure to open up a new session ! :) 

### Overview

----------
To have a generalized `time_it` function (like Python's timeit)
that would enable to take in any function that has to be timed, with proper arguments obviously. To also have other utility functions that would enable to test the `time_it` function as well as workout new neurons (biological) :)

Tests in `test_session5.py` file

---------

__Some basic metrics for `session5.py` file__

====================================


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
    (for reference):
    LOC: the total number of lines of code
    LLOC: the number of logical lines of code
    SLOC: the number of source lines of code - not necessarily corresponding to the LLOC
    comments: the number of Python comment lines (i.e. only single-line comments #)
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


-------------------------
-------------

## Code implementation and overview:

### time_it(fn, *args, repetitions= 1, **kwargs)
            **kwargs) -> Union[float, Exception]:
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


### squared_power_list
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

### polygon_area
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

### temp_converter
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


### speed_converter
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
