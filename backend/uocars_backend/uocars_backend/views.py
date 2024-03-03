from django.http import HttpResponse, JsonResponse
from math import radians, sin, cos, sqrt, atan2

def calculate_route(request):
    if request.method == 'POST':
        try:
            # Retrieve data from the POST request (model, position, destination)
            model = request.POST.get('model')
            position = request.POST.get('position')
            destination = request.POST.get('destination')
            
            # Perform route calculation logic
            distance = calculate_distance(position, destination)
            vehicle_range = get_vehicle_range(model)

            # Check if the distance exceeds the vehicle range
            if distance > vehicle_range:
                charging_stations = calculate_charging_stations(distance, vehicle_range)
            else:
                charging_stations = []

            # Construct the route data
            route_data = {
                'distance': distance,
                'charging_stations': charging_stations,
            }

            # Return the route data as a JSON response
            return JsonResponse(route_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


# Helper functions
def calculate_distance(position, destination):
    # Function to calculate distance between two coordinates using Haversine formula
    # Convert latitude and longitude from degrees to radians
    lat1, lon1 = map(radians, position)
    lat2, lon2 = map(radians, destination)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = 6371 * c  # Radius of Earth in kilometers
    return distance

def get_vehicle_range(model):
    # Dummy function to get vehicle range based on model
    # You should replace this with actual logic to retrieve range from database or any other source
    if model == 'f-150_stand':
        return 400  # Example range in kilometers for F-150 Standard Range
    elif model == 'f-150_ext':
        return 500  # Example range in kilometers for F-150 Extended Range
    elif model == 'mustang_stand':
        return 350  # Example range in kilometers for Mustang Mach-E Standard Range
    elif model == 'mustang_ext':
        return 450  # Example range in kilometers for Mustang Mach-E Extended Range
    else:
        return 0  # Unknown model

def calculate_charging_stations(distance, vehicle_range):
    # Dummy function to calculate number of charging stations needed
    # You should replace this with actual logic based on distance and vehicle range
    charging_stations_needed = distance // vehicle_range  # Example calculation
    return charging_stations_needed

# Optional functions (not implemented in this example)
def calculate_duration(distance):
    # Dummy function to calculate travel duration
    # You can implement this function if needed
    pass

def get_waypoints(position, destination):
    # Dummy function to calculate intermediate waypoints
    # You can implement this function if needed
    pass