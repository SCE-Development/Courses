## Intro to Cross Site Scripting (XSS)

Topics that will be covered:
1. What is XSS?
2. Different Types of XSS
3. Preventive Mechanisms
4. Demo
5. Learning Resources

## What is XSS?
Cross Site Scripting is an attack that injects malicious executable scripts into the code of a trusted application or website.  

Consider a search box where you can look up a database or a certain term. What happens if someone enters an executable code such as this `<script>alert('XSS');<script>`?

Yep, you guessed it right! An alert box will pop up on your screen. In the real world, this situation could be a lot more serious. It can involve things like retrieving bank details and email addresses, stealing cookies and session data, and accessing databases. 

Currently, XSS is ranked as #3 on Top 10 security threats by [OWASP](https://owasp.org/www-project-top-ten/) and is the most common web application security flaw. As web developers, we must be aware of this serious security concern and take steps to prevent it!

## Different Types of XSS
There are 3 types of Cross Site Scripting attacks:

 - Stored
	 - script is stored in the database, in cookie, session data, or a file
	 - executes later when the data is viewed or retrieved
	 - Injected script is permanently stored in the target (Databases, message forum, comment field).
 - Reflected
	 - script is in URLs or forms
	 - executes immediately when data is retrieved
	 - Injected script is reflected off of the web server (error message, search result).
 - DOM-based
	 - script is embedded in existing page or DOM
	 - executes immediately when JS event is triggered
	 - The most common source of attack is the URL

## Preventive Mechanisms
As a developer, you can prevent XSS attacks in your application by taking the following steps to:
- Encode outputs
- Sanitize and validate user-provided inputs, i.e, escaping certain characters
- Sanitize data before output
- Limit use of user-provided data

## Demo
Let's practice XSS attacks by playing Google's [XSS game](https://xss-game.appspot.com/)! Guess what type of XSS attack takes place in challenges 1-4 as you try them out. Check out this [detailed documentation](https://medium.com/bug-bounty-hunting/google-xss-game-for-beginners-5290c2f72f01) of the game in the event you get stuck. 

## What's Next?
Below, we've listed a few resources to practice and learn more about Cross Site Scripting attacks:
- Practice Exercises: [https://portswigger.net/web-security/cross-site-scripting](https://portswigger.net/web-security/cross-site-scripting)
- More Practice Exercises (Not Free): [https://pentesterlab.com/exercises](https://pentesterlab.com/exercises)
- To read more:
	-   [https://explore.bowbridge.net/blog/cybersecurity-for-sap-managers-cross-site-scripting-xss](https://explore.bowbridge.net/blog/cybersecurity-for-sap-managers-cross-site-scripting-xss)
	-  [https://www.axelerant.com/resources/team-blog/cross-site-scripting-best-practices-secure-site-xss-attack](https://www.axelerant.com/resources/team-blog/cross-site-scripting-best-practices-secure-site-xss-attack)
	- [https://medium.com/swlh/xss-for-beginners-6752b1b1487d](https://medium.com/swlh/xss-for-beginners-6752b1b1487d)
    [https://portswigger.net/web-security/cross-site-scripting](https://portswigger.net/web-security/cross-site-scripting)


Authors: Sahana Ilenchezhian & Shivani Asokumar






