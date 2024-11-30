The WebUpdatesNotifier is a little program that you can use for looking
through the HTML code of a webpage. It automatically sends you an email
notifying if there is any change.

You must take an initial look to the HTML code of the target webpage
to know where you want to search.

WebUpdatesNotifier uses BeautifulSoup to retrieve tags and its content,
that is what you have to config in the code of the program.
The the program will look everything below that code.

If you don´t stop running the program it will check the web every hour.

Feel free to make me any suggestion to improve it and do the program
yours, edit it as you like for your ownpurposes.

Contact me on developer@aralaxai.dev to discuss anything you want.

Thanks you very much and enjoy.

How to configure program:

-Add your email account settings to the code. Remember to don´t share.

-Scroll down until you arrive to the variable "url" and set it

-Once you know the tag of HTML where you want to start, replace the field
 name and string from this line:
 events = soup.find(name="h3", string="Eventos")
 
-Replace "span" with the tag you want to retrieve, it will retrieve
 all text and code from the website included on that tag. It doesn't
 matters how many times the tag is repeated, it will retrieve all.

Program will save all content from that last tag on a temp text file
to compare it with the new retrieves any time runs.
