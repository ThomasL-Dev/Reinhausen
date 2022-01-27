package com.reinhausen.computerapp.Bin.Controllers;

import com.reinhausen.computerapp.RootApplication;
import com.reinhausen.computerapp.Utils.HttpReponse;
import com.reinhausen.computerapp.Utils.HttpRequest;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class ControllerObject {


    public void initialize() {}

    public Stage GetStage(Node node){
        Stage stage = (Stage) node.getScene().getWindow();
        return stage;
    }

    public void ChangeScene(Node node, String sceneName){
        try {
            Stage stage = this.GetStage(node);
            FXMLLoader fxmlLoader = new FXMLLoader(RootApplication.class.getResource(sceneName));
            stage.setScene(new Scene(fxmlLoader.load(), 1280, 720));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public HttpReponse DoRequest(String url){
        // "http://192.168.1.20:5002/api/db/list"
        HttpRequest req = new HttpRequest(url, "POST");
        return new HttpReponse(req.GetReponse());
    }

}
