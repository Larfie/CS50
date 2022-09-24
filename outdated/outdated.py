months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    final_date = [str(x) for x in get_date()]
    print(f"{final_date[0]}-{final_date[1].zfill(2)}-{final_date[2].zfill(2)}")


def get_date():
    while True:
        date = input("Date: ")
        try:
            m, d, y = [int(x) for x in date.split("/")]
        except ValueError:
            try:
                # September 8, 1636
                m, d, y = date.split(" ")
                m = months.index(m) + 1
                if "," not in d:
                    continue
                d = int(d.replace(",",""))
                y = int(y)

            except:
                pass
            else:
                if d > 31 or m > 12 or y <= 0:
                    continue
                return [y, m, d]
        else:
            if d > 31 or m > 12 or y <= 0:
                continue
            return [y, m, d]


main()