package com.reinhausen.computerapp.Bin;

import com.reinhausen.computerapp.RootApplication;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;


public class RootStage extends Stage {


    public RootStage() throws IOException {
        this.setTitle("Reinhausen");

        FXMLLoader fxmlLoader = new FXMLLoader(RootApplication.class.getResource("admin.fxml"));
        this.setScene(new Scene(fxmlLoader.load(), 1280, 720));

        this.show();
    }

}
