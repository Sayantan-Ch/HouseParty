import React, { Component } from "react";
import CreateRoomPage from "./CreateRoomPage";
import RoomJoinPage from "./RoomJoinPage";
import { BrowserRouter, Routes, Route, Link, Redirect } from "react-router-dom";
export default class HomePage extends Component {
    constructor(props) {
      super(props);
    }
render() {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<p>This is the home page</p>}></Route>
        <Route path="/join" element={<RoomJoinPage />} />
        <Route path="/create" element={<CreateRoomPage />} />
      </Routes>
    </BrowserRouter>
  );
}


}
