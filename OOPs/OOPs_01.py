class Car:
    # Class variable to count the total number of car instances
    total_car = 0

    def __init__(self, brand, model):
        # Private attributes for brand and model
        self.__brand = brand
        self.__model = model
        # Increment the total car count whenever a new instance is created
        Car.total_car += 1

    def get_brand(self):
        # Returns the brand with a custom message
        return self.__brand + " !"

    def full_name(self):
        # Returns the full name of the car (brand and model)
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        # Default fuel type for standard cars
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        # Static method providing a general description of cars
        return "Cars are means of transport"
    
    @property
    def model(self):
        # Property to access the model of the car
        return self.__model
    
    @property
    def brand(self):
        # Property to access the brand of the car
        return self.__brand


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # Initialize the parent class (Car)
        super().__init__(brand, model)
        # Additional attribute for battery size
        self.battery_size = battery_size

    def fuel_type(self):
        # Override the fuel type method for electric cars
        return "Electric charge"


# Creating an instance of ElectricCar
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# Checking if my_tesla is an instance of Car and ElectricCar
print(isinstance(my_tesla, Car))          # Output: True
print(isinstance(my_tesla, ElectricCar))  # Output: True

# Accessing the private brand attribute via the method
print(my_tesla.get_brand())               # Output: Tesla !
print(my_tesla.fuel_type())               # Output: Electric charge

# Creating a standard car
my_car = Car("Tata", "Safari")
print(my_car.full_name())                 # Output: Tata Safari
print(my_car.general_description())        # Output: Cars are means of transport
print(my_car.model)                        # Output: Safari

# Battery and Engine classes for electric vehicles
class Battery:
    def battery_info(self):
        # Returns information about the battery
        return "This is battery"

class Engine:
    def engine_info(self):
        # Returns information about the engine
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    def __init__(self, brand, model):
        # Initialize Car, Battery, and Engine classes
        Car.__init__(self, brand, model)  # Initialize Car
        Battery.__init__(self)             # Initialize Battery
        Engine.__init__(self)              # Initialize Engine

# Creating an instance of ElectricCarTwo
my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())       # Output: This is engine
print(my_new_tesla.battery_info())      # Output: This is battery
