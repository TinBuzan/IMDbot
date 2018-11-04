# import imdb
#
# i = imdb.IMDb()
#
# movie = i.search_movie('The Truman Show')
# id = i.get_imdbID(movie[0])
# result = i.get_movie(id)
#
# actor = i.search_person('Jim Carrey')[0]
# a = actor.personID
# person = i.get_person(a)['salary']
#
# matching = [s for s in person if 'The Truman Show' in s]
# result = matching[0].split('::')[1:][0]
# # print(result)
#
#
# actorz = ['Jim Carrey',
# 'Laura Linney',
# 'Noah Emmerich',
# 'Natascha McElhone',
# 'Holland Taylor',
# 'Brian Delate',
# 'Blair Slater',
# 'Peter Krause',
# 'Heidi Schanz',
# 'Ron Taylor']
#
# az = i.search_person(actorz[0])[0]
#
# print(az)


# import imdb
# i = imdb.IMDb()
# # movie_list is a list of Movie objects, with only attributes like 'title'
# # and 'year' defined.
# movie_list = i.search_movie('the passion')
# # the first movie in the list.
# first_match = movie_list[0]
# # only basic information like the title will be printed.
# print(first_match.summary())
# # update the information for this movie.
# i.update(first_match)
# # a lot of information will be printed!
# print(first_match.summary())
# # retrieve trivia information
# i.update(first_match, 'trivia')
# print(m['trivia'])
# # retrieve both 'quotes' and 'goofs' information (with a list or tuple)
# i.update(m, ['quotes', 'goofs'])
# print(m['quotes'])
# print(m['goofs'])
# # retrieve every available information.
# i.update(m, 'all')


# Salary Stuff
# import imdb
#
# i = imdb.IMDb()
#
# movie_list = i.search_movie('The Truman Show')
# top_search = movie_list[0]
# top_id = i.get_imdbID(top_search)
# movie = i.get_movie(top_id)
#
#
# top_10_actors = []
# top_10_salaries = []
# Get Cast Salaries
# for x in range(0,10):
#     top_10_actors.append(movie['cast'][x])
#
# for x in range(0,10):
#     actor = i.search_person(str(top_10_actors[x]))[0]
#     id = actor.personID
#     all_actor_salaries = []
#     try:
#         movie_salary = [s for s in i.get_person(id)['salary'] if movie_title in s]
#         salary = movie_salary[0].split('::')[1:][0]
#         top_10_salaries.append(salary)
#     except:
#         top_10_salaries.append('')
# print(str(top_10_actors))
# print(top_10_salaries)
