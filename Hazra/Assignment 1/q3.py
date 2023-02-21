tuition = 8000

print("Year\tProjected Tuition (per semester)")
print("----------------")
for year in range(1, 6):
    tuition = tuition * 1.03  # increase by 3 percent
    print(f"{year}\t${tuition:.2f}")