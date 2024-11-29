# class
class Phone:
    def __init__(self, brand, price, color, storage_capacity):
        self.brand = brand
        self.price = price
        self.color = color
        self._storage_capacity = storage_capacity # encapsulated attribute
        
    def call(self, number):
        return f"Calling {number} from {self.brand} "
    
    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"
    
    def check_storage(self):
        return f"Storage capacity: {self._storage_capacity}gb"
    
    def storage(self):
        self._storage_capacity = 64
        return "Storage almost full!"
    
    #derived class(inheritance)
class Smartwatch(Phone):
    def __init__(self, brand, price, color, storage_capacity, fitness_features):
        super().__init__(brand, price, color, storage_capacity)
        self.fitness_features = fitness_features  # Add new attribute specific to Smartwatch
    def track_activity(self, activity):
        if activity in self.fitness_features:
            return f"Tracking your {activity} activity..."
        else:
            return f"{activity} feature not available on this smartwatch."
        
# Phone object
if __name__ == "__main__":
    phone = Phone("OPPO", "Reno 10", 546, 50)
    print(phone.call("+254709876345"))
    print(phone.check_storage())
    print(phone.storage())
    
#creating smartwatch
watch = Smartwatch("Oraimo", 40, "Black", 16, ["steps", "heart rate", "sleep"])
print(watch.call("+254708760945")) #inherited from Phone
print(watch.track_activity("steps"))
print(watch.track_activity("cycling"))    