package com.reinhausen.computerapp.Bin.Controllers;

import com.reinhausen.computerapp.Utils.ApiRoutes;
import com.reinhausen.computerapp.Utils.HttpReponse;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

import java.util.Objects;


public class LoginSceneController extends ControllerObject{

    public Label login;
    public Label pwd;
    public Label lbl_error;

    public TextField txtfield_login;
    public TextField txtfield_pwd;

    public Button btn_conn;


    public void initialize() {}


    private void Connexion() {
        String log_txt = txtfield_login.getText();
        String pwd_txt = txtfield_pwd.getText();
        HttpReponse http_reponse = this.DoRequest(String.format(ApiRoutes.CONNEXION, log_txt, pwd_txt));
        String authorisation = http_reponse.GetReponse();
        if (Objects.equals(log_txt, "admin") && Objects.equals(authorisation, "authorized")){
            this.ChangeScene(txtfield_login, "admin.fxml");
        }else {
            this.ChangeScene(txtfield_login, "base.fxml");
        }

    }


    @FXML
    private void onBtnConnClick(){
        this.Connexion();
    }


    @FXML
    private void onEnterKeyPressed(){
        this.Connexion();
    }




}
