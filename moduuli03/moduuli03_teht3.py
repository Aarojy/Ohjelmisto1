gender = input("Ilmoita biologinen sukupuoli (M/F): ")
hemoglobin = int(input("Ilmoita hemoglobiini: "))

if gender.upper() == "F":
    if hemoglobin < 117:
        print("Hemoglobiinisi on viiterajojen alapuolella")
    elif hemoglobin > 175:
        print("Hemoglobiinisi on viiterajojen yläpuolella")
    else:
        print("Hemoglobiinisi on viiterajoissa")
elif gender.upper() == "M":
    if hemoglobin < 134:
        print("Hemoglobiinisi on viiterajojen alapuolella")
    elif hemoglobin > 195:
        print("Hemoglobiinisi on viiterajojen yläpuolella")
    else:
        print("Hemoglobiinisi on viiterajoissa")
else:
    print("Virheellisesti ilmoitettu sukupuoli!")