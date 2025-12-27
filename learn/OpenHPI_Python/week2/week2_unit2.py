star_wars_movies = [  
["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],  
["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],   
["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
]
a = int(input("number of the trilogy(1,2, or 3):"))
b = int(input("number of the film(1,2, or 3):"))

print("The title of the film is:", star_wars_movies[a-1][b-1])