# Tyre Consortium Plotter
FSAE has previously provided 2022 Calspan Tire Research data for competing teams to analyze. In particular, this project is reviewing Round 9 graphing recommendations for personal analysis and automated insights. The research in question is from Project 2356.

<details>
<summary> Preamble </summary>

Round 9 consisted of cornering, drive-brake-combined, low speed transient tests, and traditional sweeps at various highway speeds. This assessed Goodyear, Hoosier, and MRF tires on 10-inch aluminum Keizer wheels and 13-inch Diamond Racing wheels.

| Preliminary Info | Purpose |
| --- | --- |
| Contents | Overview of Project 2356 |
| RunGuide | Summary of tire/rim combos and test types|
| Summary Tables | Calspan's run details |
| Raw Data (classified 'A') | All data between main test sweeps, in .mat and .dat format | 
| Run Data (classified 'B') | Removes in-between points and special test sequences, in .mat and .dat format |

Note USCS and SI unit options were provided.

`Contents` includes Transient test plan graphs, which a good plotter project will replicate to affirm consistent interpretations.

Phase 1 of the project will also seek to replicate the Cornering test plan and Drive/Brake test plan. All in all, 39 subplots to replicate across 7 plots for quality assurance. This has to be cross-referenced with `Contents`.

Phase 2 of the project will follow suggestions to plot the following:
- Lateral force v. Slip angle
- Longitudinal forcce v. Slip ratio
    - __ v. Normal Load, Inclination, Pressure, Tread Surface Temperature
- 12 psi runs comparing new tires and used tires at nominal thermal equilibrium
- Lateral force v. Slip angle during "cold to hot" sweeps
- Spring rate variation with load, inflation pressure, inclination angle, rim width, and speed
- Different rim widths as an affect on tire performance
- A very specific thing:
    - > During the transient tests, look at the distance a tire needs to roll to reach a new steady-state after a step steer. Look at the response in all force and moment channels. After a step steer at zero speed the force and moment data does not stay constant until the tire starts rolling. Why?
- Tire force and Moment performance at different speeds
- Effect of inclination angle at zero slip angle for camber sweeps
</details>

Plotting work is best decomposed into experimenting with one `.dat` file and generalizing the graphing settings to an array of filepaths.
- `version1` samples a DAT file before I understood the naming conventions, or that floating points are not observed by PyPlot until they are typecast out of the file reader's string formatting. There was good progress understanding time complexity and PyPlot settings
- `version2` gets closer to a successful replication of Transient tests across the Consortium. Graphs are producible as line and scatter plots.

Development on Plotter v1 closes with a proof-of-concept. DAT was analyzed to produce a graph, regardless of how relevant it was. The focus was moreso on how to efficiently process ~80,000 filelines as a dictionary. 
``` bash
cd version1
python3 Plotter.py  # Reads B2356.dat and creates output.png
xdg-open output.png  # A cursory search suggests this opens the PNG from terminal
```

Development on Plotter v2 closes with better code for an array of `.dat` files. Development ongoing
``` bash
cd version2
python3 Plotter.py
xdg-open transient1-1.png
```

## Developing Tyre Plotter v1
I got these takeaways from a Scientist's Programming course ..
- [ ] Time module is great when you're waiting for large datasets to be processed
- [ ] Pandas has DataFrames, great for efficiently reorganizing simple tabulated data into a dictionary structure
- [ ] Numpy has linked list arrays, much faster than your run-of-the-mill ones
- [ ] MatPlotLib has... well, plotters!
Interpreter was a first look into how badly I might need optimization developing this project. A `Timer` class is organized to instantiate and wait for two `elapse()` calls, before returning a code snippet's runtime.

The `Interpreter` class itself is tasked with understanding a `.dat` file in terms of its data columns. It's intended to provide said available columns in its `header` attribute, with the `data` attribute itself storying the DAT filelines as a dictionary.

`Plotter` is more fast and loose, a desperate attempt to understand PyPlot. In particular, graph ticks were coded without tick labels which was not easily understood on my end. Such issues are resolved by version 2.

## Developing Tyre Plotter v2
[29/06/26] Ongoing development... documenting soon...

## Closing Notes
[29/06/26] Ongoing development... documenting soon...