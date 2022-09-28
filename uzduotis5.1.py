SecConvert = 3600

MinutesGet, SecondsGet = divmod(SecConvert, 60)

HoursGet, MinutesGet = divmod(MinutesGet, 60)

print("Is viso valandu: ", HoursGet)
print("Is viso minuciu: ", MinutesGet)
print("Is viso sekundziu: ", SecondsGet)