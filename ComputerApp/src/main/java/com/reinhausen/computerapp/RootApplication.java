package com.reinhausen.computerapp;

import com.reinhausen.computerapp.Bin.RootStage;
import javafx.application.Application;
import javafx.stage.Stage;

import java.io.IOException;


public class RootApplication extends Application {

    public static void main(String[] args) {
        launch();
    }

    @Override
    public void start(Stage rootStage) throws IOException {
        new RootStage();
    }


    private void InitRootScene(){

    }


    private void StartRootSceneFileFXML(){

    }

}