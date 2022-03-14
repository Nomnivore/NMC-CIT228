import matplotlib.pyplot as plt

formats = ["PNG", "JPEG", "SVG", "GIF", "Other"]
num_used = [376, 348, 153, 104, 19]

explode = (.175, 0, 0, 0, 0)
wedgeColors = ("#FF3333", "green", "lightblue", "orange", "yellow")

fig1, ax1 = plt.subplots()
ax1.pie(num_used, explode=explode, labels=formats, colors=wedgeColors,
        startangle=-90, autopct="%1.1f%%", shadow=True)

plt.title("Popularity of Image Formats on Websites")
plt.show()
