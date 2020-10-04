from textblob.classifiers import NaiveBayesClassifier as NBC #https://en.wikipedia.org/wiki/Naive_Bayes_classifier
from textblob import TextBlob
import pickle

training = [
    ("Rock wants to sing.","Present"),
    ("Bill writes the letters.","Present"),
    ("Peter is coming to our place.","Present"),
    ("Bob has given the book to Allen.","Present"),
    ("I am going to the varsity.","Present"),
    ("Aric loves to read books.","Present"),
    ("Lisa has been living in this area for twenty years.","Present"),
    ("The singer is singing nicely.","Present"),
    ("The program is going on smoothly.","Present"),
    ("Alice prefers coffee to tea.","Present"),
   
    ("Bill attended the program.","Past"),
    ("Tom performed in the show.","Past"),
    ("Alice was practicing on the tennis court.","Past"),
    ("Jim had been there a long time ago.","Past"),
    ("I was waiting for my friends.","Past"),
    ("Peter had been cooking the meal before we reached there.","Past"),
    ("Alana was happy to hear the news.","Past"),
    ("Jeff had left the place before we reached.","Past"),
    ("Rock was singing in the show.","Past"),
    ("Bob was playing football in the field.","Past"),
    
    
    ("I will give a speech in the program.","Future"),
    ("Robert will be going to the varsity.","Future"),
    ("Tom will have reached the place by now.","Future"),
    ("I will be singing modern songs in the program.","Future"),
    ("I will help you to do the project.","Future"),
    ("Alice will assist you in this case.","Future"),
    ("We will have reached home before you come.","Future"),
    ("Robin will come to our place.","Future"),
    ("Alana will sing country songs in the program.","Future"),
    ("Bob will write a poem.","Future")
     
]

test = [
    ("Alana attends the class every day.","Present"),
    ("Tom is talented enough to do the task.","Present"),
    ("The actor is talented.","Present"),
    ("We are excited to go to the picnic.","Present"),
    ("We have been trying to solve the problem for two hours.","Present"),

    ("They were practicing cricket for the upcoming tournament.","Past"),
    ("Alex was excited to go to the concert.","Past"),
    ("Dana wrote the letter.","Past"),
    ("I was attending the class.","Past"),
    ("I prepared the design.","Past"),

    ("Ben will do the assignment.","Future"),
    ("Henry will be traveling to Italy in March.","Future"),
    ("I will meet you in the evening.","Future"),
    ("We will watch a movie this Friday.","Future"),
    ("Patrick will have been cooking the meal before you reach home.","Future")
    
]

model = NBC(training)

print(model.classify("Patrick is going to the library."))
print(model.classify("Albert was sick."))
print(model.classify("Dona will prepare the dessert."))

print("\nTest ",model.accuracy(test)*100,"%")
print("Train:",model.accuracy(training)*100,"%")

with open(r"model.pickle", "wb") as output_file:
    pickle.dump(model, output_file)