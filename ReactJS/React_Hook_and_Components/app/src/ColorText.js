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
