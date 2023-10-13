import numpy as np
import matplotlib.pyplot as plt
import statistics
x=np.array([2,4,6,8])
y=np.array([1,5,9,3])
x_mean=statistics.mean(x)
y_mean=statistics.mean(y)
print(x-x_mean)
z=(x-x_mean)*(y-y_mean)
print(z)
z_sum=sum(z)
t=(x-x_mean)*(x-x_mean)
t_sum=sum(t)
print(t_sum)
b1=z_sum/t_sum
print(b1)
b0=y_mean-b1*x_mean
y_cap=b1*x+b0
print(b1)
print(b0)
print(y_cap)
plt.plot(y_cap)
font1={'color':'red'}
font2={'color':'orange'}
plt.title("Linear Regression",fontdict=font1)
