import matplotlib.pyplot as plt
import numpy as np

def transform_to_int(time: str) -> int:
    times = time.split(":")
    return int(times[0])*60 + int(times[1])

# data = [
#     (240.00 , "35:10"),
#     (241.90 , "34:58"),
#     (244.00 , "34:48"),
#     (248.40 , "34:10"),
#     (244.50 , "34:45"),
#     (247.30 , "34:12"),
#     (248.10 , "34:13"),
#     (242.30 , "34:55"),
#     (247.10 , "34:15"),
#     (243.80 , "34:40"),
#     (241.20 , "35:05"),
#     (246.60 , "34:30"),
#     (240.60 , "35:08"),
#     (245.80 , "34:28"),
#     (239.70 , "35:15"),
#     (243.40 , "34:52"),
#     (241.80 , "35:00"),
#     (246.00 , "34:20"),
#     (245.50 , "34:25"),
#     (246.20 , "34:25"),
#     (242.70 , "34:53"),
#     (243.60 , "34:47"),
#     (247.40 , "34:18"),
#     (242.90 , "34:50"),
#     (244.20 , "34:42"),
#     (240.90 , "35:02"),
#     (242.50 , "34:56")
# ]

# data = [
#     (245.47 , "6:54"),
#     (245.53 , "6:54"),
#     (245.42 , "6:54"),
#     (245.54 , "6:53"),
#     (245.47 , "6:54"),
#     (245.53 , "6:54"),
#     (245.42 , "6:54"),
#     (245.46 , "6:54"),
#     (242.52 , "6:53"),
#     (245.47 , "6:54"),
#     (245.53 , "6:53"),
#     (245.42 , "6:54"),
#     (245.54 , "6:53"),
#     (245.47 , "6:54"),
#     (245.53 , "6:54"),
#     (245.42 , "6:54"),
#     (245.46 , "6:54"),
#     (242.52 , "6:53"),
#     (245.47 , "6:54"),
#     (245.53 , "6:53"),
#     (245.42 , "6:54"),
#     (245.54 , "6:53"),
#     (245.60 , "6:53"),
#     (245.53 , "6:53"),
#     (245.42 , "6:54"),
#     (245.46 , "6:54"),
#     (242.52 , "6:53"),
#     (245.41 , "6:54"),
#     (245.53 , "6:53"),
#     (245.42 , "6:54"),
#     (245.54 , "6:53")
# ]


data = [
    (245.06 , "13:49"),
    (244.71 , "13:50"),
    (244.70 , "13:50"),
    (245.07 , "13:49"),
    (245.10 , "13:49"),
    (245.03 , "13:49"),
    (245.07 , "13:49"),
    (244.89 , "13:50"),
    (245.09 , "13:49"),
    (245.03 , "13:49"),
    (245.02 , "13:49"),
    (245.05 , "13:49"),
    (245.03 , "13:49"),
    (245.06 , "13:49"),
    (245.09 , "13:49"),
    (245.03 , "13:49"),
    (244.74 , "13:50"),
    (245.01 , "13:49"),
    (245.09 , "13:49"),
    (245.09 , "13:49"),
    (245.03 , "13:49"),
    (244.90 , "13:50"),
    (245.06 , "13:49"),
    (245.02 , "13:49"),
    (245.03 , "13:49"),
    (244.79 , "13:50"),
    (245.08 , "13:49"),
    (245.03 , "13:49"),
    (244.94 , "13:50"),
    (245.06 , "13:49"),
    (245.09 , "13:49")
]


speed = [i[0] for i in data]
time = [transform_to_int(i[1]) for i in data]

plt.plot([i for i in range(len(data))], speed, marker='o')
plt.title("Velocidade em KiB/s")
plt.show()

plt.plot([i for i in range(len(data))], time, marker='o')
plt.title("Tempo de transferência em segundos")
plt.show()

print(f"A média do tempo de transferência é {np.mean(time)}")
print(f"O desvio padrão do tempo de transferência é {np.std(time)}")
print(f"A variância do tempo de transferência é {np.var(time)}")

print(f"A média da velocidade é {np.mean(speed)}")
print(f"O desvio padrão da velocidade é {np.std(speed)}")
print(f"A variância da velocidade é {np.var(speed)}")