import React, { Component } from 'react';
import { Form, Message } from 'semantic-ui-react';

import './Login.css';

class Login extends Component {
  handleChange = (e, { name, value }) => this.setState({ [name]: value });

  login() {
    const { username, password } = this.state;

    console.log(username, password);
  }

  render() {
    return (
      <div className="container">
        <div className="card">
          <h1>Login</h1>
          <Form onSubmit={this.login.bind(this)}>
            <Form.Input
              fluid
              name="username"
              label="Username"
              placeholder="Username"
              onChange={this.handleChange}
            />
            <Form.Input
              fluid
              name="password"
              label="Password"
              type="password"
              placeholder="Password"
              onChange={this.handleChange}
            />
            <Form.Button primary>Submit</Form.Button>
            <Message success header="Login Successful" />
            <Message error header="Invalid login" />
          </Form>
        </div>
      </div>
    );
  }
}

export default Login;
