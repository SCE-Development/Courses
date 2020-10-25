import React, {useState} from 'react';
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