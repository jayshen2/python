import numpy as np
import matplotlib.pyplot as plt

# 1. 生成随机行走数据
np.random.seed(42)
n_people = 2000
n_steps = 100000
steps = np.random.choice([-1, 1], size=(n_people, n_steps))
pos = np.cumsum(steps, axis=1)

# 2. 计算核心指标
max_dist = np.max(np.abs(pos), axis=1)
first_step = np.argmax(np.abs(pos) == max_dist[:, None], axis=1) + 1
count_max = np.sum(np.abs(pos) == max_dist[:, None], axis=1)

# 3. 可视化（英文标题，无字体警告）
plt.figure(figsize=(10, 4))
idx_far = np.argmax(max_dist)
plt.plot(pos[idx_far], linewidth=0.5)
plt.title(f'Trajectory of the farthest walker (Max distance: {max_dist[idx_far]})')
plt.xlabel('Steps'), plt.ylabel('Position'), plt.grid(alpha=0.3)
plt.show()