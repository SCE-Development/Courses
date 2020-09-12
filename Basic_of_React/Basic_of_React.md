# Basic of `ReactJS`
React helps intergrate Javascripts, HTML, and CSS together with ez.

## Everything we will need:
1. `src/App.js` or any js file in src/
2. `src/App.css` or any css file in src/

Expecting in `App.js`:
```js
import React from 'react';
import './App.css';                   //import empty css file that you created

function App() {
 return (
   <div>
    html
   </div>
 );
}
export default App;
```

<br/>

# Syntax
## Variable
```js
import React from 'react';
import './App.css';

function App() {

  let variable = "My Name is Potato"

  return (
    <div>
      {variable}
    </div>
  );
}

export default App;
```

### Output:
![image](https://user-images.githubusercontent.com/18486562/92979198-c6e4e880-f446-11ea-889b-7cde8fe4133b.png)

<br/>

## Function returning variables
```js
import React from 'react';
import './App.css';

function App() {

  function test() {
    return "Return String"
  }

  return (
    <div>
      {test()}
    </div>
  );
}

export default App;
```

### Output:
![image](https://user-images.githubusercontent.com/18486562/92979396-5ab6b480-f447-11ea-821f-c5516baf1f8c.png)

<br/>

## Function returning html element
```js
import React from 'react';
import './App.css';

function App() {

  function test(someInput) {
    return <p> {someInput} </p>
  }

  return (
    <div>
      {test("TESTING FUNCTION INPUT")}
    </div>
  );
}

export default App;
```

### Output:
![image](https://user-images.githubusercontent.com/18486562/92979546-e9c3cc80-f447-11ea-8395-94c54bde29b6.png)

<br/>
<br/>

# CSS Syntax

## Classic CSS
```js
import React from 'react';
import './App.css';

function App() {

  return (
    <div>
      <p id = 'p1'> TEST 1 </p>
      <p className = 'p2'> TEST 2 </p>
    </div>
  );
}

export default App;
```

In `App.css`
```css
#p1 {
  color: red;
}

.p2 {
  color: blue;
}
```

### Output:
![image](https://user-images.githubusercontent.com/18486562/92982271-3c09eb00-f452-11ea-8673-a96fb8083aac.png)

<br/>

## Embed/Variable CSS
```js
import React from 'react';
import './App.css';

function App() {

  let style1 = {
    color: 'red',
    fontWeight: 'bold'
  }

  return (
    <div>
      <p style = {style1}> TEST 1 </p>
      <p style = {{color:'blue', fontWeight: 'bold'}}> TEST 2 </p>
    </div>
  );
}

export default App;
```

### Output:
![image](https://user-images.githubusercontent.com/18486562/92982453-13362580-f453-11ea-8090-04e7f96611f1.png)

<br/>

## Attribute CSS
```js
import React from 'react';
import './App.css';

function App() {

  return (
    <div>
      <p> TEST 1 </p>
      <p test='ok' > TEST 2 </p>
    </div>
  );
}

export default App;
```

In `App.css`
```css
p {
  color: red;
}

p[test='ok'] {
  color: blue;
}
```

### Output:
![image](https://user-images.githubusercontent.com/18486562/92982271-3c09eb00-f452-11ea-8673-a96fb8083aac.png)

<br/>
<br/>

# Basic Events (With [React-Hook](https://reactjs.org/docs/hooks-intro.html))

## OnClick - Element
```js
import React, {useState} from 'react';              //<-------add useState
import './App.css';

function App() {

  const [myCoolVar, setMyCoolVar] = useState (0)
  function click() {
    setMyCoolVar(myCoolVar+1)
  }

  return (
    <div>
      <p> {myCoolVar} </p>
      <button onClick={()=>{click()}}> CLICK ME </button>
    </div>
  );
}

export default App;
```

### Output:

Original

![image](https://user-images.githubusercontent.com/18486562/92983052-14b51d00-f456-11ea-8ff5-65fc7cba8a60.png)

After click

![image](https://user-images.githubusercontent.com/18486562/92983065-24ccfc80-f456-11ea-8dac-21072a5ccee9.png)

<br/>

## Onchange - Input
```js
import React, {useState} from 'react';              //<-------add useState
import './App.css';

function App() {

  //variable to keep track
  const [myCoolVar, setMyCoolVar] = useState ('default value goes in here')

  return (
    <div>
      <p> {myCoolVar} </p>
      <input onChange={(event)=>{setMyCoolVar(event.target.value)}}/>
    </div>
  );
}

export default App;
```

### Output:

Original

![image](https://user-images.githubusercontent.com/18486562/92982891-129e8e80-f455-11ea-806b-93f823b7d4ef.png)

New Input

![image](https://user-images.githubusercontent.com/18486562/92982942-4974a480-f455-11ea-805c-3427b618b8c3.png)