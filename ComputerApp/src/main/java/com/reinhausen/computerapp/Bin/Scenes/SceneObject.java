package com.reinhausen.computerapp.Bin.Scenes;

import com.reinhausen.computerapp.Utils.HttpReponse;
import com.reinhausen.computerapp.Utils.HttpRequest;
import javafx.scene.Node;
import javafx.scene.layout.GridPane;

public class SceneObject extends GridPane {


    public SceneObject() {

    }


    public void AddToScene(Node obj){
        // add button as child of the scene
        this.getChildren().add(obj);
    }


    public HttpReponse DoRequest(String url){
        // "http://192.168.1.20:5002/api/db/list"
        HttpRequest req = new HttpRequest(url, "POST");
        return new HttpReponse(req.GetReponse());
    }



}