import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './AppClass';
import { Route, Link, BrowserRouter as Router } from 'react-router-dom' //import routing
import Profile from './Profile.js'    //Import our profile page

const routing = (
  <Router>
    <div>
      <Route exact path="/" component={App} />
      <Route path="/profile" component={Profile} />
    </div>
  </Router>
)

ReactDOM.render(
  routing,
  document.getElementById('root')
);
