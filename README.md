# Marketplace_Flask

#Marketplace is a project that i am building for my Python course graduation. I got my help from https://www.youtube.com/@jamalbugti9957, Codemy.com youtube channel and freeCodeCamp.org. 

The project is made with Flask framework, with the help of bootstrap framework combined with jinja syntax. All the information regarding user credentials and items available in the database is stored using SQLite database.

Main button links that are within the project structure are:
	- Home,
	- Products,
	- Register,
	- Login. 

In the "Home" page a user can find the welcome message, the site logo, the navbar with the main buttons and the "Get started" button that redirect a logged in user to the "Product" page. If the user is not logged in, then it will be redirected to the "Login" page.

In the "Login" page, a user that already has created an account can login, and access the remaning products that are available on the site.
In order for a user to login, it is neccessary the Username and the Password credentials to be completed.
Also in case that a user does not have an account or he wish to create another account, there is a "Register" button that redirects to the "Register" page.

In the "Register" page, a user can create a new account by completing the following fields: "User Name", "Email Address", "Password" and "Confirm password".
After the registration is successfuly, the user has access to the "Products" page where it is automatically redirected.


Under the "Products" page it can be found 4 categories according to products: 
		- Laptops,
		- TV's,
		- Tablets,
		- SmartPhones.
	 A user can buy a product from any category and then cancel his order by "selling" the product back to the market.

	
