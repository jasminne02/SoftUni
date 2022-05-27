petrolPumpsNumber = int(input())

for pump in range(petrolPumpsNumber):
    command = input().split(' ')
    petrolAmount = int(command[0])
    distanceKm = int(command[1])  # distance from that petrol pump to the next

