import matplotlib.pyplot as plt
#linear graph
'''x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y,color='green',linestyle='dashdot',marker='o')
plt.title('simple line graph')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()'''

#pie chart
labels=['pyramid','shady side of pyramid','sky']
sizes=[25,5,70]
colors=['#c2b280','#8b7d6b','lightblue']
plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=215)
plt.title('pyramid')
plt.axis('equal')
plt.show()

'''import matplotlib.pyplot as plt
x=[20,30,45]
y=[13,24,56]
plt.plot(x,y)
plt.title('summa')
plt.xlabel('xaxis')
plt.ylabel("yaxis")
plt.show() '''

"""x="subject"
y="marks"
plt.bar(x,10)
plt.barh(y,20)
plt.xlabel("maths")
plt.ylabel("sciene")
plt.show()
"""
         