package com.reinhausen.computerapp.Bin.Controllers;


import javafx.fxml.FXML;
import javafx.scene.control.Label;


public class AdminSceneController {

    @FXML
    public Label onglet_name;

    public void initialize() {
        onglet_name.setText("test");

    }


}
