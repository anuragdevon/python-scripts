# Designing a low level design of a parking system
# Using Object Oriented Programming

# Assumptions:
# 1. The parking lot is a rectangular grid
# 2. The parking lot has multiple levels
# 3. The parking lot can park motorcycles, cars, and buses
# 4. The parking lot has motorcycle spots, compact spots, and large spots
# 5. A motorcycle can park in any spot
# 6. A car can park in either a single compact spot or a single large spot
# 7. A bus can park in five large spots that are consecutive and within the same level
# 8. If the parking lot is full, then vehicles must leave in order of arrival
# 9. Each vehicle can only park in one spot at a time
# 10. A bus can park in as many consecutive large spots as possible

class Vehicle:
    def __init__(self, vin):
        self.vin = vin
        self.parkingSpot = None

    def getVin(self):
        return self.vin

    def getParkingSpot(self):
        return self.parkingSpot

    def setParkingSpot(self, parkingSpot):
        self.parkingSpot = parkingSpot

    def clearParkingSpot(self):
        self.parkingSpot = None

class Bus(Vehicle):
    def __init__(self, vin):
        super().__init__(vin)
        self.size = 'large'

    def getSize(self):
        return self.size

    def park(self, parkingLot):
        if parkingLot.parkBus(self):
            self.setParkingSpot(parkingLot.getBusSpot())
            return True
        return False

    def clear(self, parkingLot):
        parkingLot.clearBusSpot(self.getParkingSpot())
        self.clearParkingSpot()

    def __str__(self):
        return 'Bus: ' + self.getVin()

    def __repr__(self):
        return self.__str__()

class Car(Vehicle):
    def __init__(self, vin):
        super().__init__(vin)
        self.size = 'compact'

    def getSize(self):
        return self.size

    def park(self, parkingLot):
        if parkingLot.parkCar(self):
            self.setParkingSpot(parkingLot.getCarSpot())
            return True
        return False

    def clear(self, parkingLot):
        parkingLot.clearCarSpot(self.getParkingSpot())
        self.clearParkingSpot()

    def __str__(self):
        return 'Car: ' + self.getVin()

    def __repr__(self):
        return self.__str__()

class Motorcycle(Vehicle):
    def __init__(self, vin):
        super().__init__(vin)
        self.size = 'motorcycle'

    def getSize(self):
        return self.size

    def park(self, parkingLot):
        if parkingLot.parkMotorcycle(self):
            self.setParkingSpot(parkingLot.getMotorcycleSpot())
            return True
        return False

    def clear(self, parkingLot):
        parkingLot.clearMotorcycleSpot(self.getParkingSpot())
        self.clearParkingSpot()

    def __str__(self):
        return 'Motorcycle: ' + self.getVin()

    def __repr__(self):
        return self.__str__()

class ParkingLot:
    def __init__(self, numLevels, numMotorcycleSpots, numCompactSpots, numLargeSpots):
        self.numLevels = numLevels
        self.numMotorcycleSpots = numMotorcycleSpots
        self.numCompactSpots = numCompactSpots
        self.numLargeSpots = numLargeSpots
        self.numSpots = numMotorcycleSpots + numCompactSpots + numLargeSpots
        self.levels = []
        self.createLevels()

    def createLevels(self):
        for i in range(self.numLevels):
            self.levels.append(Level(i + 1, self.numMotorcycleSpots, self.numCompactSpots, self.numLargeSpots))

    def parkBus(self, bus):
        for level in self.levels:
            if level.parkBus(bus):
                return True
        return False

    def parkCar(self, car):
        for level in self.levels:
            if level.parkCar(car):
                return True
        return False

    def parkMotorcycle(self, motorcycle):
        for level in self.levels:
            if level.parkMotorcycle(motorcycle):
                return True
        return False

    def clearBusSpot(self, busSpot):
        busSpot.clear()

    def clearCarSpot(self, carSpot):
        carSpot.clear()

    def clearMotorcycleSpot(self, motorcycleSpot):
        motorcycleSpot.clear()

    def getBusSpot(self):
        for level in self.levels:
            for spot in level.getSpots():
                if isinstance(spot, BusSpot):
                    return spot
        return None

    def getCarSpot(self):
        for level in self.levels:
            for spot in level.getSpots():
                if isinstance(spot, CarSpot):
                    return spot
        return None

    def getMotorcycleSpot(self):
        for level in self.levels:
            for spot in level.getSpots():
                if isinstance(spot, MotorcycleSpot):
                    return

    def getSpots(self):
        spots = []
        for level in self.levels:
            spots += level.getSpots()
        return spots

    def __str__(self):
        return 'ParkingLot: ' + str(self.numLevels) + ' levels, ' + str(self.numSpots) + ' spots'

    def __repr__(self):
        return self.__str__()

class Level:
    def __init__(self, levelNum, numMotorcycleSpots, numCompactSpots, numLargeSpots):
        self.levelNum = levelNum
        self.numMotorcycleSpots = numMotorcycleSpots
        self.numCompactSpots = numCompactSpots
        self.numLargeSpots = numLargeSpots
        self.numSpots = numMotorcycleSpots + numCompactSpots + numLargeSpots
        self.spots = []
        self.createSpots()

    def createSpots(self):
        for i in range(self.numMotorcycleSpots):
            self.spots.append(MotorcycleSpot(self, i + 1))
        for i in range(self.numCompactSpots):
            self.spots.append(CarSpot(self, i + 1))
        for i in range(self.numLargeSpots):
            self.spots.append(LargeSpot(self, i + 1))

    def parkBus(self, bus):
        for spot in self.spots:
            if spot.park(bus):
                return True
        return False

    def parkCar(self, car):
        for spot in self.spots:
            if spot.park(car):
                return True
        return False

    def parkMotorcycle(self, motorcycle):
        for spot in self.spots:
            if spot.park(motorcycle):
                return True
        return False

    def clear(self):
        for spot in self.spots:
            spot.clear()

    def getSpots(self):
        return self.spots

    def __str__(self):
        return 'Level: ' + str(self.levelNum) + ' with ' + str(self.numSpots) + ' spots'

    def __repr__(self):
        return self.__str__()

class Spot:
    def __init__(self, level, spotNum):
        self.level = level
        self.spotNum = spotNum
        self.vehicle = None

    def park(self, vehicle):
        if self.vehicle == None:
            self.vehicle = vehicle
            return True
        return False

    def clear(self):
        self.vehicle = None

    def getLevel(self):
        return self.level

    def getSpotNum(self):
        return self.spotNum

    def getVehicle(self):
        return self.vehicle

    def __str__(self):
        return 'Spot: ' + str(self.level.getLevelNum()) + '-' + str(self.spotNum)

    def __repr__(self):
        return self.__str__()

class BusSpot(Spot):
    def __init__(self, level, spotNum):
        super().__init__(level, spotNum)
        self.size = 'bus'

    def getSize(self):
        return self.size

    def __str__(self):
        return 'BusSpot: ' + str(self.level.getLevelNum()) + '-' + str(self.spotNum)

    def __repr__(self):
        return self.__str__()

class CarSpot(Spot):
    def __init__(self, level, spotNum):
        super().__init__(level, spotNum)
        self.size = 'car'

    def getSize(self):
        return self.size

    def __str__(self):
        return 'CarSpot: ' + str(self.level.getLevelNum()) + '-' + str(self.spotNum)

    def __repr__(self):
        return self.__str__()

class MotorcycleSpot(Spot):
    def __init__(self, level, spotNum):
        super().__init__(level, spotNum)
        self.size = 'motorcycle'

    def getSize(self):
        return self.size

    def __str__(self):
        return 'MotorcycleSpot: ' + str(self.level.getLevelNum()) + '-' + str(self.spotNum)

    def __repr__(self):
        return self.__str__()

class LargeSpot(Spot):
    def __init__(self, level, spotNum):
        super().__init__(level, spotNum)
        self.size = 'large'

    def getSize(self):
        return self.size

    def __str__(self):
        return 'LargeSpot: ' + str(self.level.getLevelNum()) + '-' + str(self.spotNum)

    def __repr__(self):
        return self.__str__()

def main():
    parkingLot = ParkingLot(1, 10, 10, 10)
    bus = Bus('123456789')
    car = Car('987654321')
    motorcycle = Motorcycle('123456789')
    bus.park(parkingLot)
    car.park(parkingLot)
    motorcycle.park(parkingLot)
    print(parkingLot)
    bus.clear(parkingLot)
    car.clear(parkingLot)
    motorcycle.clear(parkingLot)
    print(parkingLot)