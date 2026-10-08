# CSPC - PW1 Lab A: Reproducible Foundations: Environment, Git & GitHub
### Test Results

All 3 tests passed successfully

### Speed Comparison

Data: N0 = 200000; lam = 0.4; dt = 0.01, steps = 100; seed = 0

First Trial:
    Python time: 2.6925235749986314 seconds
    NumPy time: 0.00030630500259576365 seconds
    Differnce: 8790.334967372388 times
Second Trial:
    Python time: 2.7274901180026063 seconds
    NumPy: 0.000295623998681549 secons
    Differnce: 9226.21346767149 times
Third Trial:
    Python time: 2.687192540997785seconds
    NumPy time: 0.0002924350010289345 seconds
    Differnce: 9189.025019381674 times

### Conclusion

NumPy works much more faster than Python especially considering bigger numbers.

# CSPC - PW1 Lab B: Data, Plotting and Automation

### What I Did

1. Checked and installed the required tools and packages for Lab B, such as `matplotlib` and `snakemake`.

2. Loaded and worked with the observed decay data from the provided file.

3. Calculated the analytical decay values using the given decay law.

4. Created a plot comparing the observed data with the analytical decay curve using `matplotlib` and saved it as `figure.png`.

5. Used Snakemake to automate the plotting process and learned about the advantages of workflow automation.

### What the Data Showed

The observed data show a decrease in the number of atoms over time, which is consistent with the expected behaviour of radioactive decay.

### Comparison with the Analytical Law

The observed data approximately follow the analytical decay curve. There are some differences between the observed values and the analytical curve, which are expected because the observed decay process has a stochastic nature.

### Conclusion

During this laboratory work, I studied the basic features of `matplotlib` and the advantages of `Snakemake`. It was interesting to explore data visualization by creating a plot of the observed data and the analytical decay curve. I also learned that Snakemake can create a consistent and reproducible pipeline, which helps automate and organize computational tasks.

# CSPC - PW2 Lab A: Motion from Tracking Data

### What I did

1. Checked and installed the required tools and packages for Lab B, such as `scipy`

2. Loaded and worked with the observed decay data from the provided file.

3. Calculated the `gradient` of position and velocity parameters, and the mean value of acceleration (-8.5797 m/s2).

4. Computed the integratad values of accleration and velocity by usind `cumulative_trapezoid` method and found `max_diff` between `original` and `recovered` positions.

5. Created a plot which illustrates the dependence of position, velocity and acceleration on time, added additional options to it, and saved the resulted image as `motion.png`.

### What the Data Showed

The observed data show the affect of `noise` on finding the mean value of acceleration. Also demonstrates the behaviour of free parameters (y, v, a) which were found by gradient and trapezoid methods, on a certain time interval. Moreover, by finding the `max_diff` value it can be clearly seen thet it correlates to the value less than 1 meter, which is acceptable for our investigation.

### Conclusion

While doing this laboratory work I studied about `scipy` and its advantages, increased my level of knowledge at creating subplots and diagrams by using new useful features of `matplotlib` such as: adding `colors` or `linestyles` and so on. Furthermore, I learned about `np.gradient` and the advatage of`cumulative_trapezoid` command that allows us to surpress the noise observed earlier.
