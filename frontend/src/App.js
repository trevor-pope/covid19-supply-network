import React, { Component } from "react";
import { BrowserRouter as Router, Route, Redirect } from "react-router-dom";

import TopBar from "./TopBar/TopBar";
import BottomBar from "./BottomBar/BottomBar";
import Login from "./Tabs/Login/Login";
import Cookie from "universal-cookie";

import "./App.css";

import "semantic-ui-css/semantic.min.css";

class App extends Component {
  render() {
    const cookies = Cookie()
    const loggedIn
    if (cookies.get("currentUser") == null)
      loggedIn = false
    else
      loggedIn = true

    return (
      <Router>
        <div className="App">
          <TopBar />
          <div id="content">
            <Route exact path="/" render={() => <Redirect to="/raw" />} />
            <Route path="/login" component={Login} />
          </div>
          <BottomBar />
        </div>
      </Router>
    );
  }
}

export default App;
