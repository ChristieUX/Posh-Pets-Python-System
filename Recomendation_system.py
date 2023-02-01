def pet_selection(): # Defined function for the pet selection question.

    pet_types = ['Dog', 'Cat', 'Rabbit', 'Parrot', 'Hamster', 'Tortois', 'Turtle', 'Lizard'] # List for types of pets
    
    users_pet = input("What type of pet do you have? ").title()
    
    if users_pet in pet_types: # If statment as to wether user input is within list
        print(f"Great lets move on to more quetions about your {users_pet}.")
        
        if users_pet.title() == "Dog":
            large_breed = input("Is it a large breed? ")
            if large_breed.title() == "Yes":
                large_breed_yes = input("So you have a large breed, I bet they are a handfull. We just need to know if its a puppy? ")
                if large_breed_yes.title() == "Yes":
                    print("A large breed puppy, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")
                else:
                    print("A large breed adult, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")           
            else:
                large_breed_no = input("So you have a small breed, We just need to know if its a puppy? ")
                if large_breed_no.title() == "Yes":
                    print("A small breed puppy, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")
                else:
                    print("A small breed adult, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")
        
        elif users_pet.title() == "Cat":
            large_breed = input("Is it a adult cat? ")
            if large_breed.title() == "Yes":
                print("So you have a adult cat, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")
            else:
                print("So you have a kitten, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")

        elif users_pet.title() == "Rabbit":
            adult_rabbit = input("Is it a adult rabbit? ")
            if adult_rabbit.title() == "Yes":
                print("So you have a adult rabbit, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")
            else:
                print("So you have a baby rabbit, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")               

        elif users_pet.title() == "Parrot":
            adult_parrot = input("Is it a adult parrot? ")
            if adult_parrot.title() == "Yes":
                print("So you have a adult parrot, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")
            else:
                print("So you have a baby parrot, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")
        
        elif users_pet.title() == "Hamster":
            adult_hamster = input("Is it a adult hamster? ")
            if adult_hamster.title() == "Yes":
                print("So you have a adult hamster, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")
            else:
                print("So you have a baby hamster, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")
        
        elif users_pet.title() == "Tortois":
            adult_tortois = input("Is it a adult tortois? ")
            if adult_tortois.title() == "Yes":
                print("So you have a adult tortois, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")
            else:
                print("So you have a baby tortois, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")

        elif users_pet.title() == "Turtle":
            adult_turtle = input("Is it a adult turtle? ")
            if adult_turtle.title() == "Yes":
                print("So you have a adult turtle, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")
            else:
                print("So you have a baby turtle, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")


        elif users_pet.title() == "Lizard":
            adult_lizard = input("Is it a adult lizard? ")
            if adult_lizard.title() == "Yes":
                print("So you have a adult lizard, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")
            else:
                print("So you have a baby lizard, how nice! Your custom Poshpets product selection is being specially tailored as we speak.")

    else: # Else statement explaining
        print("Im very sorry but we only support the top eight main house pets currently, refer to the list below:")
        print(', '.join(pet_types))
        user_start_again = input("Would you like to input another pet type? ").title()
        if user_start_again.title() == "Yes": # End pet type questioning as app doesnt support pet type
            pet_selection() # Itterate back to initial user input for pet type
        else:
            print("Ok, please keep an eye out for updates on our supported pet types.")

pet_selection()
