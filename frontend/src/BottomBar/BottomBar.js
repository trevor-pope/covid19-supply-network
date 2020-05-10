import React, { Component } from 'react';
import { Menu } from 'semantic-ui-react';
import { NavLink } from 'react-router-dom';

class BottomBar extends Component {
  render() {
    return (
      <Menu>
        <Menu.Item as={NavLink} to="/login" activeClassName="active">
          Login
        </Menu.Item>
        <Menu.Item
          as={NavLink}
          to="/raw"
          position="right"
          activeClassName="active"
        >
          View Raw Data
        </Menu.Item>
      </Menu>
    );
  }
}

export default BottomBar;
