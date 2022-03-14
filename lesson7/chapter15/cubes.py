import matplotlib.pyplot as plt

squared = []
inputVal = [1, 2, 3, 4, 5]
raised = []

for num in inputVal:
    squared.append(num*num*num)
    raised.append(num**2)

# plot 1
ax1 = plt.subplot(1, 2, 1)
plt.style.use("bmh")
ax1.plot(inputVal, squared, marker="o", ls="--", color="red")
plt.title("Cubed Numbers")
plt.ylabel("Values Squared")
plt.xlabel("Input Values")
plt.grid()

# plot 2
ax2 = plt.subplot(1, 2, 2)
plt.style.use("seaborn")
ax2.plot(inputVal, raised, c="purple", lw="2", ls="-.", marker="^")
plt.title("Numbers Raised")
plt.ylabel("Second Power")
plt.xlabel("Input Values")
plt.grid()


plt.suptitle("Fun with Numbers")
plt.subplots_adjust(top=0.8, wspace=1)
plt.show()
