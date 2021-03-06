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

## Mapping Array
```js
import React, {useState} from 'react';
import './App.css';

function App() {

  let array = [
    {name: "Beth", age: 2},
    {name: "Smith", age: 4}
  ]

  return (
    <div>
      {array.map((val)=>{
        return <p>{val.name}: {val.age}</p>
      })}
    </div>
  );
}

export default App;
```

### Output:
![image](https://user-images.githubusercontent.com/18486562/98305563-f14eb000-1f76-11eb-81f6-47c393ca28c6.png)

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