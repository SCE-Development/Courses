# React Hook, Components, and Event Listeners

## Everything we will need:
1. `src/App.js` or any js file in src/
2. `src/ColorText.js` or any js file in src/

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

<br>
<br>
<br>
<br>

# Components
Sometimes we want to create our own components. Lets say we want to pass the `myCoolVar` to another components for processing. Lets make a new component `src/ColorText.js` first!

In `src/ColorText.js`:
```js
import React, {useState} from 'react';

function ColorText(props) {

  const style = {
    color: props.myCoolVar
  }

  return (
    <div>
      <p> Another component</p>
      <p style = {style}> {props.myCoolVar} </p>
    </div>
  );
}

export default ColorText;
```

where `props` is the propagated data/variable from one component to another. Lets now import this `ColorText.js` to our `App.js`

<br>
<br>

In `src/App.js`, import `ColorText.js` and call its tag:
```js
import React, {useState} from 'react';
import './App.css';

import ColorText from './ColorText'         //<-Import

function App() {

  //variable to keep track
  const [myCoolVar, setMyCoolVar] = useState ('default value goes in here')

  return (
    <div>
      <p> {myCoolVar} </p>
      <input onChange={(event)=>{setMyCoolVar(event.target.value)}}/>

      <ColorText myCoolVar = {myCoolVar} ></ColorText>    <!--Call Tag-->

    </div>
    )
}

export default App;
```

We imported `ColorText.js` with 
```js 
import ColorText from './ColorText' 
```

We called `ColorText` with
```js 
<ColorText myCoolVar = {myCoolVar} ></ColorText>
```
and passes the variable `myCoolVar` to the `ColorText` component that we created.

### Result
![2020-10-25-17-08-58](https://user-images.githubusercontent.com/18486562/97122716-39531480-16e5-11eb-9d67-7bbe00a3a56d.png)

![2020-10-25-17-09-16](https://user-images.githubusercontent.com/18486562/97122717-39ebab00-16e5-11eb-9d97-eebddf5e62dc.png)

![2020-10-25-17-09-33](https://user-images.githubusercontent.com/18486562/97122718-39ebab00-16e5-11eb-980c-1fc5049b5e5f.png)

![2020-10-25-17-10-40](https://user-images.githubusercontent.com/18486562/97122719-3a844180-16e5-11eb-8191-d44a4bb1efbe.png)

