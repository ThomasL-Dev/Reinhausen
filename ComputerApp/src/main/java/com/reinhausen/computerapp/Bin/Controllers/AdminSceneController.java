package com.reinhausen.computerapp.Bin.Controllers;


import com.reinhausen.computerapp.Utils.ApiRoutes;
import com.reinhausen.computerapp.Utils.HttpReponse;
import javafx.beans.value.ObservableValue;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;

import java.util.Arrays;


public class AdminSceneController extends ControllerObject {

    public TabPane tabpane_db;
    public ListView<String> list_db_admin_pan;


    public void initialize() {
        this.InitDbList();
        this.InitDbListListener();
    }



    private void CreateTabs(String dbname, String tables){



        // delete tabs to not overcreate
        this.DeleteTabs();

        for (String table : tables.split(", ")){
            // create Tab Object for each tables
            Tab tab = new Tab();
            tab.setText(table);

            // create db info column container
            TableView<String> table_view_container = new TableView<String>();

            // create table columns
            HttpReponse http_reponse = this.DoRequest(String.format(ApiRoutes.TABLE_COLUMNS, dbname, table));
            String columns = http_reponse.GetReponse();
            for (String column : columns.split(", ")) {
                TableColumn<String, String> table_column = new TableColumn<>(column);
                table_view_container.getColumns().add(table_column);
            }

            // construct it
            tab.setContent(table_view_container);
            tabpane_db.getTabs().add(tab);
        }

    }

    private void DeleteTabs(){
        tabpane_db.getTabs().removeAll(tabpane_db.getTabs());
    }



    private void InitDbList(){
        HttpReponse http_reponse = this.DoRequest(ApiRoutes.DB_LIST);
        String reponse = http_reponse.GetReponse();

        for(String db : reponse.split(", ")){
            list_db_admin_pan.getItems().add(db);
        }
    }

    private void InitDbListListener(){
        list_db_admin_pan.getSelectionModel().selectedItemProperty().addListener((ObservableValue<? extends String> ov, String old_val, String new_val) -> {
            String selected_db = list_db_admin_pan.getSelectionModel().getSelectedItem();

            HttpReponse tables_http_reponse = this.DoRequest(String.format(ApiRoutes.DB_TABLES, selected_db));
            String tables_from_db = tables_http_reponse.GetReponse().replace(selected_db, "").replace("tables", "").replace("db", "").replace(", , , ", "");

            this.CreateTabs(selected_db, tables_from_db);

        });
    }
}
