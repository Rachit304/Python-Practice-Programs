import pandas as pd

data = pd.read_csv("D:\MCA 1\PYTHON - MCA 171\Practicals\datafile.csv")

while 1:
    print("-----------------------")
    print("Select Any one operation u want...")
    print("1.Remove record with Empty Data\n2.Group Records by Country")
    print("3.Most Expensive wine in Spain\n4.Find Average of each country..")
    print("5.Exit")
    choice = int(input("Enter Ur Choice: "))

    if choice == 1:
        print(data.dropna())
    elif choice == 2:
        Country = data.groupby(['country'])
        for Key, item in Country:
            print("Country name  is:", Key)
            print(item, "\n\n")
    elif choice == 3:
        Spain = data.loc[data['country'] == 'Spain']
        max_price = Spain.max()
        print(max_price[["country", "description", "price", "winery"]])
    elif choice == 4:
        Country = data.groupby(['country'])
        avg = Country["points"].mean()
        avg.columns = ['country', 'Mean']
        print(avg)
    elif choice == 5:
        break
    else:
        print("Invalid Input")
