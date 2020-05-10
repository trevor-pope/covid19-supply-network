import React, { Component } from "react";
import { Menu } from "semantic-ui-react";
import { NavLink } from "react-router-dom";

class TopBar extends Component {
  render() {
    return (
      <Menu widths={3}>
        <Menu.Item as={NavLink} to="/box" activeClassName="active">
          Box Plot
        </Menu.Item>
        <Menu.Item as={NavLink} to="/scatter" activeClassName="active">
          Scatter Plot
        </Menu.Item>
        <Menu.Item as={NavLink} to="/time" activeClassName="active">
          Time Series Graph
        </Menu.Item>
      </Menu>
    );
  }
}

export default TopBar;
