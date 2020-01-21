import matplotlib.pyplot
import csv

data_file = "../sam_assignment_1_pose_data.csv"

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file)
    x_data = []
    y_data = []

    for row in csv_reader:
        try:
            x_data.append(float(row[0]))
            y_data.append(float(row[1]))
        except Exception as e:
            print(e)

    matplotlib.pyplot.title("X and Y position data scatter plot")
    matplotlib.pyplot.scatter(x_data, y_data)


matplotlib.pyplot.show()
