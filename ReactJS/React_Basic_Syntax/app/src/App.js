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