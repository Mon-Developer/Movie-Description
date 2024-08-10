from tkinter import *
import imdb


#Functionalities part

def search():
    root1=Toplevel()
    root1.geometry('900x550+70+60')
    root1.title('Movie Information')
    root1.config(bg='orange')


    title_label=Label(root1,text='Title',font=('cooper black',20,'bold'),fg='white',bg='orange',bd=0)
    title_label.place(x=60,y=50)
    title_label=Label(root1,font=('algerian',20,'bold'),fg='white',bg='orange')
    title_label.place(x=300,y=50)


#Director label
    director_label=Label(root1,text="Director:",font=('cooper black',20,'bold'),fg='white',bg='orange')
    director_label.place(x=60,y=100)
    director_label=Label(root1,font=('algerian',20,'bold'),fg='white',bg='orange')
    director_label.place(x=300,y=100)

#Year label
    year_label=Label(root1,text='Year',font=('cooper black',20,'bold'),fg='white',bg='orange',bd=0)
    year_label.place(x=60,y=170)
    year_label=Label(root1,font=('algerian',20,'bold'),fg='white',bg='orange',bd=0)
    year_label.place(x=300,y=165)

#Runtime label
    runtime_label=Label(root1,text='Runtime:',font=('cooper black',20,'bold'),fg='white',bg='orange',bd=0)
    runtime_label.place(x=60,y=240)
    runtime_label=Label(root1,font=('algerian',20,'bold'),fg='white',bg='orange',bd=0)
    runtime_label.place(x=300,y=235)    


#Genres label
    genres_label=Label(root1,text='Genres:',font=('cooper black',20,'bold'),fg='white',bg='orange',bd=0)
    genres_label.place(x=60,y=280)
    genres_label=Label(root1,font=('algerian',20,'bold'),fg='white',bg='orange',bd=0)
    genres_label.place(x=300,y=310)    


#Rating label
    rating_label=Label(root1,text='Rating:',font=('cooper black',20,'bold'),fg='white',bg='orange',bd=0)
    rating_label.place(x=60,y=380)
    rating_label=Label(root1,font=('algerian',15,'bold'),fg='white',bg='orange',bd=0)
    rating_label.place(x=300,y=380)  


#Cast label

    cast_label=Label(root1,text='Cast:',font=('cooper black',15,'bold'),fg='white',bg='orange',bd=0)
    cast_label.place(x=60,y=450)
    cast_label=Label(root1,font=('algerian',15,'bold'),fg='white',bg='orange',bd=0,wraplength=615) #wraplength for multiply lines
    cast_label.place(x=300,y=450)  

   
#Object of imdb class imdb.IMDB((object):
  #  def __init__(self, *args):
   #     super(imdb.IMDB(, self).__init__(*args))
    
    
    imdb_object=imdb.IMDb()
    movie_name=movieEntry.get()
   # print(movie_name)
    movies=imdb_object.search_movie(movie_name)
    #movies=imdb_object.search(movie_name)
    #print(movies)
    index=movies[0].getID()
    print(index)
    movie=imdb_object.get_movie(index)
    #print(movie)
    title=movie['title']
    title_label.config(text=title)

    year=movie['year']
    year_label.config(text=year)
    
    director=movie['director']
    director_label.config(text=director)
     #for director in movie['director']:
        #director_label.config(text=director)

    genres=movie['genres']
    genres_label.config(text=genres)

    rating=movie['rating']
    rating_label.config(text=rating)



    cast=movie['cast']
    #cast_label.config(text=cast)
    castlist=list(map(str,cast))
    #print(castlist)
    slicelist=castlist[:10]  #only 10 casts show here
    #print(slicelist)
    #cast_label.config(text=slicelist)
    st=''
    for i in slicelist:
        st=st+i

    cast_label.config(text=st)    


   # runtime=movie['runtime']
   # runtime_label.config(text=runtime)
    for runtime in movie['runtime']:
        hours=int(runtime)//60
        minutes=int(runtime)%60
   
        runtime_label.config(text=f'{hours} hour {minutes} minutes')





    root1.mainloop()



#GUI part
root=Tk()




root.geometry('950x600+50+30')
root.title('Movie Descriptions')
root.resizable('True','False')

bgpic=PhotoImage(file='C:/Users/WELCOME PC/Desktop/Movie Desc/moviepic/h28.png')
#lbl=Label(image=bgpic).pack()


bgLabel=Label(root,image=bgpic)
bgLabel.place(x=95,y=5)#(width=1050,height=600)

movieLabel=Label(root,text="Movie Name:",font=('algerian',33,'bold'),bg='whitesmoke',bd=3)
movieLabel.place(x=100,y=530)

movieEntry=Entry(root,font=('FELIX TITLING',23,'bold'),bd=5,relief=GROOVE,justify='center')
movieEntry.place(x=390,y=535)
movieEntry.focus_set()


moviesearch_Button=Button(root,text='Search',font=("FELIX TITLING",15,'bold'),bd=3,relief='groove',command=search)
moviesearch_Button.place(x=810,y=535)





root.mainloop()