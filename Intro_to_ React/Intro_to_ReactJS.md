# Intro To `ReactJS`
Tools we will use:
1. [NodeJS](https://nodejs.org/en/)
2. ReactJS
3. [Visual Studio Code (IDE)](https://code.visualstudio.com/)
4. ***Optional*** - I recommend [git bash terminal](https://git-scm.com/downloads) for `window` users, but the normal `cmd terminal` is also fine.

Check for installation using terminal, as long as a `version` is visible - you are good:

NodeJS
   ``` shell
    node --version
   ```
   ![node version](https://user-images.githubusercontent.com/18486562/92313825-f302f400-ef84-11ea-9b24-87e93f8668b4.png)

Notice: `NodeJS` should also provide you `npm` and `npx`.
   ``` shell
      npm --version
      npx --version
   ```
   ![npm npx version](https://user-images.githubusercontent.com/18486562/92313829-08781e00-ef85-11ea-9fa6-e2e6226a71af.png)

<br></br><br></br>

# Create your project

   In the terminal, in your desired working directory (run one by one):

   ``` shell
      npx create-react-app my-app
      cd my-app
      npm install
      npm start
   ```

   More info at ReactJS [website](https://reactjs.org/docs/create-a-new-react-app.html)

   ## Your project should start at [http://localhost:3000/](http://localhost:3000/)

   ![react home](https://user-images.githubusercontent.com/18486562/92313832-0f069580-ef85-11ea-953f-a7ac8b245e5f.png)

<br></br><br></br>

# CODING TIMEEE

   In your app's directory:

   ``` shell
      code .
   ```

   or open the working directory in your VSCode.

   <br></br>
   ![vs studio](https://user-images.githubusercontent.com/18486562/92313836-15950d00-ef85-11ea-9526-332ed2bd65e9.png)
   <br></br>

<br></br><br></br>

# Purging Nonsense

   Delete these 4 files

   ![delete](https://user-images.githubusercontent.com/18486562/92313840-1f1e7500-ef85-11ea-9138-a5d79f88bae8.png)

   <br></br>

   ***Remember:*** `ctrl + s` to save, React will render any changes that you made.

   <br></br>

   In `index.js`, delete these lines:
   ```js

      import React from 'react';
      import ReactDOM from 'react-dom';
      import './index.css';
      import App from './App';
      import * as serviceWorker from './serviceWorker';                                //<------Delete

      ReactDOM.render(
        <React.StrictMode>
          <App />
        </React.StrictMode>,
        document.getElementById('root')
      );

      // If you want your app to work offline and load faster, you can change
      // unregister() to register() below. Note this comes with some pitfalls.
      // Learn more about service workers: https://bit.ly/CRA-PWA
      serviceWorker.unregister();                                                      //<------Delete

   ```

   to

   ```js

      import React from 'react';
      import ReactDOM from 'react-dom';
      import './index.css';
      import App from './App';

      ReactDOM.render(
        <React.StrictMode>
          <App />
        </React.StrictMode>,
        document.getElementById('root')
      );

   ```

   <br></br>

In `App.js`, delete these lines:
```js
   import React from 'react';
   import logo from './logo.svg';                     //<------Delete
   import './App.css';

   function App() {
     return (
       <div className="App">
         <header className="App-header">
           <img src={logo} className="App-logo" alt="logo" />              <!-- <<------Delete --> 
           <p>
             Edit <code>src/App.js</code> and save to reload.
           </p>
           <a
             className="App-link"
             href="https://reactjs.org"
             target="_blank"
             rel="noopener noreferrer"
           >
             Learn React
           </a>
         </header>
       </div>
     );
   }

   export default App;
```

to

```js
   import React from 'react';
   import './App.css';

   function App() {
     return (
       <div className="App">
         <header className="App-header">
           <p>
             Edit <code>src/App.js</code> and save to reload.
           </p>
           <a
             className="App-link"
             href="https://reactjs.org"
             target="_blank"
             rel="noopener noreferrer"
           >
             Learn React
           </a>
         </header>
       </div>
     );
   }

   export default App;
```
<br></br><br></br>

# Creating a new component (page)

Let's make a Profile. Create `Profile.js` under `src`, directory: `src/Profile.js`

![2020-09-04-15-24-47](https://user-images.githubusercontent.com/18486562/92313843-234a9280-ef85-11ea-8b8b-e1e1ae748b7a.png)

<br></br>

In `src/Profile.js`:
```js
import React from 'react';

   export default function Profile() {
       return (
           <div>
               
               HTML IN HERE

               Example:

               <h1>HI! My name is THAI</h1>

               BIO:
               <ul>
                   <li>I like to breathe</li>
                   <li>I lost too much money in the stock market please help :(</li>
                   <li>IDK what to write here</li>
               </ul>

           </div>
       );
   }
```

***Notes:*** ReactJS support `HTML` within `Javascript` files. I suggest familiarize yourself with [HTML](https://www.w3schools.com/html/) and [JS](https://www.youtube.com/watch?v=W6NZfCO5SIk). 

If you notice, within this `Profile` function (aka method), `HTML` is written within the `return` box. It is very common to `return` a `HTML component` in `JS function`.

<br></br><br></br>

# Routing to new pages

Let's install a new routing package for ReactJS. In shell:

```shell

   `ctrl + c` to cancel react server
   npm install react-router-dom
   npm start

```

In `src/index.js`, import `react-router-dom` and `create routes`:

```js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { Route, Link, BrowserRouter as Router } from 'react-router-dom';  //Import react-router-dom
import Profile from './Profile.js';  //Import our Profile.js page

//Generating routes
const routing = (
  <Router>
    <div>
      <Route exact path="/" component={App} />
      <Route path="/profile" component={Profile} />
    </div>
  </Router>
)

//Render routes
ReactDOM.render(
  routing,
  document.getElementById('root')
);
```

## Navigate to Profile with [http://localhost:3000/profile](http://localhost:3000/profile)

![profile](https://user-images.githubusercontent.com/18486562/92314409-09607e00-ef8c-11ea-8eed-952b44787a67.png)

## We're done!

You just made your first react-page! Here is a [great tutorial](https://www.youtube.com/watch?v=Ke90Tje7VS0) if you are interested.