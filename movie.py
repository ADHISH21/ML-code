# loading the data from the csv file to apandas dataframe
movies_data = pd.read_excel(r"C:\Users\nikhi\OneDrive\Documents\new_movies.xlsx")
null_threshold=2000
null_counts = movies_data.isnull().sum()
columns_to_remove = null_counts[null_counts > null_threshold].index
movies_data=movies_data.drop(columns=columns_to_remove)
movies_data.info()
movies_data.to_csv()
selected_features = ['genres','keywords','CAST','DIRECTOR']
for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')
ch = int(input('''Enter 1 for Genre based recommendation \n 
                   Enter 2 for cast based recommendation \n 
                   Enter 3 for director based recommendation \n 
                   Enter 4 for story based recommendation \n 
                   Enter 5 for Genre and Cast based recommendation \n 
                   Enter 6 for Genre and director based recommendation \n 
                   Enter 7 for Genre and story based recommendation \n 
                   Enter 8 for Cast and Director based recommendation \n                   
                   Enter 9 for Cast and Story based recommendation \n
                   Enter 10 for Director and Story based recommendation \n
                   Enter 11 for Genre, Cast and Director based recommendation \n
                   Enter 12 for Story, Cast and Director based recommendation \n
                   Enter 13 for Genre, Story and Director based recommendation \n
                   Enter 14 for Genre, Cast and Story based recommendation \n
                   Enter 15 for Best Case movie recommendation \n'''))

if ch==1:
    cc=movies_data['genres']
elif ch==2:
    cc=movies_data['CAST']
elif ch==3:
    cc=movies_data['DIRECTOR']
elif ch==4:
    cc=movies_data['keywords']
elif ch==5:
    cc=movies_data['genres']+' '+movies_data['CAST']
elif ch==6:
    cc=movies_data['genres']+' '+movies_data['DIRECTOR']
elif ch==7:
    cc=movies_data['genres']+' '+movies_data['keywords']
elif ch==8:
    cc=movies_data['DIRECTOR']+' '+movies_data['CAST']
elif ch==9:
    cc=movies_data['keywords']+' '+movies_data['CAST']
elif ch==10:
    cc=movies_data['keyword']+' '+movies_data['DIRECTOR']
elif ch==11:
    cc=movies_data['genres']+' '+movies_data['CAST']+' '+movies_data['DIRECTOR']
elif ch==12:
    cc=movies_data['keywords']+' '+movies_data['CAST']+' '+movies_data['DIRECTOR']
elif ch==13:
    cc=movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['DIRECTOR']
elif ch==14:
    cc=movies_data['genres']+' '+movies_data['CAST']+' '+movies_data['keywords']
elif ch==15:
    cc= movies_data['genres']+' '+movies_data['CAST']+' '+movies_data['DIRECTOR']+' '+movies_data['keywords'] 
else:
    print("Invalid Input")
    
    
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(cc)
similarity = cosine_similarity(feature_vectors)
movie_name = str(input(' Enter your favourite movie name : '))
list_of_all_titles = [str(title) for title in movies_data['title'].tolist()]
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
close_match = find_close_match[0]
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
similarity_score = list(enumerate(similarity[index_of_the_movie]))
len(similarity_score)
sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

print('Movies suggested for you : \n')

i = 1
x=input("Number of reccomendations?")
y=int(x)+1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<int(y)):
    print(i, '.',title_from_index)
    i+=1
