import math
from statsmodels.stats.power import TTestIndPower

effect_size = 0.5  # Medium effect size
alpha = 0.05       # Significance level
power = 0.8        # Desired power

analysis = TTestIndPower()
sample_size = analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, alternative='two-sided')

print(f"Calculated sample size: {sample_size}")


# Round up to the nearest multiple of 25
rounded_sample_size = math.ceil(sample_size / 25) * 25

print(f"Rounded sample size (multiple of 25): {rounded_sample_size}")