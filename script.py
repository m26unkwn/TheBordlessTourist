destinations=["Paris, France","Shanghai, China","Los Angeles, USA","Sao Paulo, Brazil","Cairo, Egypt"] #defined destinations where people choose the destination 

test_traveler=['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']] #this is a test_traveler schema if a traveler choose any destination the data of the traveler will be in the following manner


def get_destination_index(destination): #function to get the destination index
    destination_index=destinations.index(destination)# using .index() function 
    return (destination_index) #returned destination index


def get_traveler_location(traveler): #function to get the location of travler
    traveler_destination=traveler[1] # assigned index from the schema where test_traveler location is at first index
    traveler_destination_index=get_destination_index(traveler_destination)
    return traveler_destination_index

attractions = []
for destination in destinations:
    attractions.append([])

def add_attraction(destination,attraction):
    try:
        destination_index=get_destination_index(destination)
        attractions_for_destination=attractions[destination_index].append(attraction)
    except SyntaxError:
        return

    
add_attraction("Los Angeles, USA",['Venice Beach',['beach']])
#addded few attraction to the attraction list
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])    


print(attractions)
