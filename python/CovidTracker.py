import tkinter as tk

from matplotlib.pyplot import show

root = tk.Tk()
root.geometry("350x350")
root.title("Covid-Data-Country-wise")

def showData():
    from matplotlib import pyplot as plt
    import matplotlib.patches as mpatches
    from covid import Covid

    covid = Covid()
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []

    try:
        root.update()
        countries = data.get()
        country_names = countries.strip()
        country_names = country_names.replace(" ", ",")
        country_names = country_names.split(",")
        
        for country in country_names:
            cases.append(covid.get_status_by_country_name(country))
            root.update()
        for case in cases:
            confirmed.append(case["confirmed"])
            active.append(case["active"])
            deaths.append(case["deaths"])
            recovered.append(case["recovered"])
        
        # addding patches...
        confirmed_patch = mpatches.Patch(color="green", label="confirmed")
        recovered_patch = mpatches.Patch(color="red", label="recovered")
        active_patch = mpatches.Patch(color="red", label="active")
        deaths_patch = mpatches.Patch(color="black", label="deaths")

        plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch])

        for x in range(len(country_names)):
            plt.bar(country_names[x], confirmed[x], color="green")
            if recovered[x] > active[x]:
                plt.bar(country_names[x], recovered[x], color="red")
                plt.bar(country_names[x], active[x], color="blue")
            else:
                plt.bar(country_names[x], active[x], color="blue")
                plt.bar(country_names[x], recovered[x], color="red")
        
        plt.title("Current Covid Cases")
        plt.xlabel("Country Name")
        plt.ylabel("Cases in Millions")
        plt.show()

    except:
        print("Enter correct details")

tk.Label(root, text="Enter countries names\n whose covid data you want").pack()
tk.Label(root, text="Country Name:").pack()
data = tk.StringVar()
data.set("India")
entry = tk.Entry(root, textvariable=data, width=50).pack()
tk.Button(root, text="Get Data", command=showData).pack()
root.mainloop()