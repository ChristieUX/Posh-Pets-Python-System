
def geopy():

# import module
    from geopy.geocoders import Nominatim
    
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="Pet Tracker - CTaPs")
    
    
    # Latitude & Longitude input from gps tracker
    Latitude = "51.4870373811307"
    Longitude = "-2.517114961266722"
    
    location = geolocator.reverse(Longitude+", "+Latitude)
    
    address = location.raw['address']

address = ["Fishponds", "BS16", "3GY"]

# List of all stored pet users, and pet stores on the Poshpets system
def animals_stores():
    
    cat_sb = ["Snowball the cat in Brislington", 'BS3']
    dog_tgy = ["Taggy the dog in Hillfields Park", 'BS16']
    lizard_rlph = ["Ralph the lizard in Lawrence Weston", 'BS11']
    rabbit_bky = ["Blinky the rabbit in Bradley Stoke", 'BS32']
    dog_frda = ["Freeda the dog in Fishponds", 'BS16']
    cat_wne = ["Winnie the cat in Emersons green", 'BS16']
    cat_ble = ["Billie the cat in Fontwell Dr", 'BS16']
    dog_grg = ["George the dog in Bromley heath", 'BS16']

    full_pet_list = [cat_sb, dog_tgy, lizard_rlph, rabbit_bky, dog_frda, cat_wne, cat_ble, dog_grg]
    
    pets_ah = ["Pets at home", "BS34"]
    shggy = ["Shaggy dog pet suppliers", "BS13"]
    petshop = ["The pet shop", "BS16"]
    rep_em = ["Bristol reptile emporium", "BS30"]
    oll_poll = ["Ollys Pollys", "BS3"]
    dog_hse = ["Dog house", "BS8"]
    farleys = ["Farleys pet food and garden supplies", "BS16"]
    evry_day = ["Everyday pet & birds", "BS7"]

    full_store_list = [pets_ah, shggy, petshop, rep_em, oll_poll, dog_hse, farleys, evry_day]

    user_choice = input("Would you like to know pets nearby or just nearby stores? ")

    if user_choice == 'pets':
        print(f"You are close to:")
        for i in full_pet_list:
            for a in i:
                if a == address[1]:
                    print(', '.join(i))
   
    else:
        print(f"You are close to:")
        for i in full_store_list:
            for a in i:
                if a == address[1]:
                    print(', '.join(i))

animals_stores()
        