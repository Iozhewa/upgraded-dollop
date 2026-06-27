# Tyre Consortium Plotter
FSAE has previously provided 2022 Calspan Tire Research data for competitor teams to analyze. In particular, this project is reviewing Round 9 graphing recommendations for personal analysis and automated insights. The research in question is from Project 2356.

<details>
<summary> Preamble </summary>

Round 9 consisted of cornering, drive-brake-combined, low speed transient tests, and traditional sweeps at various highway speedes. This assessed Goodyear, Hoosier, and MRF tires on 10-inch aluminum Keizer wheels and 13-inch Diamond Racing wheels.

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

[28/06/26] Ongoing development... documenting soon...