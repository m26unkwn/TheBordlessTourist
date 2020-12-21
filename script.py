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

#find the best places to go

def find_attractions(destination,interests):
    destination_index=get_destination_index(destination)
    attractions_in_city=attractions[destination_index]
    attractions_with_interest=[]
    for attraction in attractions_in_city:
        possible_attraction=attraction
        attraction_tags=attraction[1]
        
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])

    return attractions_with_interest


def attractions_for_traveler(traveler):
    traveler_destination=traveler[1]
    traveler_interest=traveler[2]
    traveler_attractions=find_attractions(traveler_destination,traveler_interest)
    interesting_string="Hi " + traveler[0] +", we think you'll like these places around " + traveler_destination + ": "

    for i in range(len(traveler_attractions)):
        if traveler_attractions[-1]==traveler_attractions[i]:
            interesting_string+="the " + traveler_attractions[i] +'.'

        else:
            interesting_string+="the "+ traveler_attractions[i] + ', '


    return interesting_string


france_smile=attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(france_smile)
