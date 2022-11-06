"""1. Consider influenza epidemics for 2-person families.
The probability is 21% that at least one has disease.
The probability that the husband has contracted influenza is 15% while the
probability that both the wife and husband have contracted the disease is 10%.
What is the probability that the wife has influenza? """

# P(mother or father) = P(mother) + P(father) - P(mother and father)
# P(mother) = P(mother or father) + P(mother and father) - P(father)
P_AorB = 0.21
P_A = 0.15
P_AB = 0.1

Pm = P_AorB + P_AB - P_A
print(f"The probability that the wife has influenza {Pm * 100} %")
