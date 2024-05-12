import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.randint(100, size=(5))
print(x)
x1 = random.choice([3, 5, 7, 9], size=(3, 5))
print(x1)
x2 = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x2)
x3 = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x3)
y = random.rand(5)
print(y)
z = random.randint(100, size=(3, 5))
print(z)
z1 = random.rand(3, 5)
print(z1)
arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)
print(random.permutation(arr))

sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()

#Normal Distribution
a = random.normal(size=(2, 3))
print(a)
a1 = random.normal(loc=1, scale=2, size=(2, 3))
print(a1)
sns.distplot(random.normal(size=1000), hist=False)
plt.show()

#Binomial Distribution
b = random.binomial(n=10, p=0.5, size=10)
print(b)
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()

#comparison between normal and binomial distribution
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()

#Poisson Distribution
c = random.poisson(lam=2, size=10)
print(c)
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()
#comparison between normal and poisson distribution
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
plt.show()
#comparison between poisson and binomial distribution
sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')
plt.show()

#Uniform Distribution
d = random.uniform(size=(2, 3))
print(d)
sns.distplot(random.uniform(size=1000), hist=False)
plt.show()

#Logistic Distribution
e = random.logistic(loc=1, scale=2, size=(2, 3))
print(e)
sns.distplot(random.logistic(size=1000), hist=False)
plt.show()

#comparison between uniform and logistic distribution
sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')
plt.show()

#multinomial distribution
f = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(f)

#exponential distribution
g = random.exponential(scale=2, size=(2, 3))
print(g)
sns.distplot(random.exponential(size=1000), hist=False)
plt.show()

#chi square distribution
h = random.chisquare(df=2, size=(2, 3))
print(h)
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()

#Rayleigh Distribution
i = random.rayleigh(scale=2, size=(2, 3))
print(i)
sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()

#pareto distribution
j = random.pareto(a=2, size=(2, 3))
print(j)
sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show()

#Zipf distribution
k = random.zipf(a=2, size=(2, 3))
print(k)
x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)
plt.show()