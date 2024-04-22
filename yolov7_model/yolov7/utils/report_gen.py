import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# save result to csv that contain three feature: objectname, confidence, and box_location
def saveToCSV(filePath, objName, confidence, obj_bbox):
    with open(filePath + ".csv", 'a', encoding='utf8') as f:
        save = csv.writer(f)
        save.writerow([objName, confidence, obj_bbox])
        f.close()

# splite object name and confidence from previous method to store in saveToCSV
def splitText(text):

    a = text.split(': ')

    return a[0], a[1]

# additional function to create a box plot for visualizing objects detected
def SummaryObject(filePath, outputResultPath):
    df = pd.read_csv(filePath +".csv", names=['object_name', 'confidence'])
    df = df.sort_values('object_name')

    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    
    sns.boxplot(y = 'object_name', x = 'confidence', data=df)
    plt.title('Summary Object Detection vs Confidence')
    plt.savefig(outputResultPath + '.jpg')
