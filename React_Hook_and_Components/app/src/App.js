import React, {useState} from 'react';
import './App.css';

import ColorText from './ColorText'

function App() {

  //variable to keep track
  const [myCoolVar, setMyCoolVar] = useState ('default value goes in here')

  return (
    <div>
      <p> {myCoolVar} </p>
      <input onChange={(event)=>{setMyCoolVar(event.target.value)}}/>

      <ColorText myCoolVar = {myCoolVar} ></ColorText>

    </div>
    )
}

export default App;