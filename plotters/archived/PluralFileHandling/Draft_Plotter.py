#!/usr/bin/env python3

class Timer:
    '''
    Provides time complexity analysis with elapse.
    '''
    pass

class Parser:
    '''
    Provides DataFrame reconstruction of DAT files.
    '''
    pass

class Plotter:
    '''
    Provides PyPlot representation of DataFrames.
    '''
    pass

class Interpreter:
    '''
    Provides Parser/Plotter sequencing by reading sequence instructions (INI?).

    e.g.
        [Transient Velocity Tests]
            paths = a.dat, b.dat, c.dat
            measure = ET, 4
            creates = a.png, b.png, c.png
            or creates = SUBPLOTS
            graphing=line
            or graphing=scatter, 0.001
            axis = ET, V
            xTicks = 0, 1100, 200
            yTicks = -5, 35, 5
        [Transient Normal Load Tests]
            ...
        [Transient Inclination Angle Tests]
            ...
        ...
    '''
    pass