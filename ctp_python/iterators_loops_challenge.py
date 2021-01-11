def run():
    pass

hour = 0
minutes = 0

while hour < 25:   # 24 hour
    while minutes < 61:   # 60 minutes
        print(f"Hour: {hour}, Mins: {minutes}") #end=" ")
        minutes += 1

    hour += 1
    minutes = 0
    print("\n")


if __name__ == "__main__":
    run()

# hora = 0
# minuto = 0
# segundo = 0  

# while hora < 24:
#     while minuto < 60:
#         while segundo < 60:
#             print(hora, minuto, segundo)
#             segundo += 1
#         minuto += 1
#         segundo = 0
#     hora += 1
#     minuto = 0