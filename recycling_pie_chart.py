# added on 2/8/24
import matplotlib.pyplot as plt

def pie_chart():
    numbers = [20, 20, 20, 20,20]
    labels = ['Plastic', 'Aluminum', 'Paper', 'Steel','Cardboard']
  

    fig1, ax1 = plt.subplots()
    ax1.pie(numbers, labels=labels)
    plt.show()
  


if __name__ == '__main__':
    pie_chart()
