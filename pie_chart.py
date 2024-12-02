import matplotlib.pyplot as plt

plt.style.use("ggplot")

roles = [    
    "Front-end", 
    "Back-end",
    "Full-stack",
    "DevOps"
    ]

employees = [52,36,28,11]

plt.pie(employees, labels=roles, autopct="%.2f%%", explode=[ 0.1, 0, 0, 0])
plt.show()