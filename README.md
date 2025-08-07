# wikipedia-cli-bot

# requirements
pip install wikipedia
wikipedia is the main library. installing it will install all the dependencies. full list in requirements.txt

# how to use

## search menu
you start in the search menu. start by entering a search term.
bot will return 5 suggested pages based on the search term.
you can also type 'random' for a list of 10 random articles.
you can exit by typing quit or exit.
select a page by entering the number.

## page menu
you are now in the "page" menu. select the number to view the summary, sections, links, or go back to the search menu.
entering the summary options will print the page summary and list the page menu
entering the sections option will take you to the sections menu. See wikipedia.py bug below.
entering the links options will print the links and list the page menu
entering the back option will go back to the search menu

## sections menu.
you are now in the sections menu. the sections are listed numerically.
select back option to go back to the page menu
select the number to view the contents of that section. doesn't always work.
after print the section, you are taken back to the page menu

# sample usage
```
Enter a search term. Type 'random' for 10 random articles. To leave, type 'exit' or 'quit'.


>>> star wars

Please choose a page:
1. Star Wars
2. List of Star Wars films  
3. Star Wars (film)
4. Star Wars: The Clone Wars
5. Star Wars: Clone Wars    

>>> 1

Choose an option:
1. Page Summary 
2. Page Sections
3. Page Links   
0. Back

>>> 1
Summary for 'Star Wars':
Star Wars is an American epic space opera media franchise created by George Lucas...

Choose an option:
1. Page Summary
2. Page Sections
3. Page Links
0. Back

>>> 2 

Sections for 'Star Wars':
1. Premise
2. Films
3. The Skywalker Saga
...
0. Back

>>> 1

Star Wars : Premise

The Star Wars franchise depicts the adventures of characters "a long time ago in a galaxy far, far away"...

Choose an option:
1. Page Summary
2. Page Sections
3. Page Links
0. Back

>>> 0

Enter a search term. Type 'random' for 10 random articles. To leave, type 'exit' or 'quit'.


>>> exit
Goodbye!
```


# wikipedia.py bug
there is a bug in the wikipedia library. page.sections does not work out of the box.
to fix, in wikipedia.py, replace:

ln 646: 
query_params.update(self.__title_query_param)

with:
query_params.update({'page': self.title})
