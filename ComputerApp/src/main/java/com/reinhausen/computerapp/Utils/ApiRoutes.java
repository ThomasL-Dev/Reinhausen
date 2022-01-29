package com.reinhausen.computerapp.Utils;

public class ApiRoutes {
    /*
    *  les "%s" sont des parametres a utilisé avec String.format(string, param)
    * */

    protected static String SERVER_URL = "http://92.157.253.9:5002";

    // connect or not user
    public static String CONNEXION =  SERVER_URL + "/api/connect/%s/%s";

    // recup toute les DB
    public static String DB_LIST =  SERVER_URL + "/api/db/list";
    // recup les tables de la DB donné en parametre
    public static String DB_TABLES =  SERVER_URL + "/api/db/%s";
    // recup les colones de la table donné
    public static String TABLE_COLUMNS =  SERVER_URL + "/api/db/%s/table/%s/columns";
    // recup les données dune table dans une DB
    public static String TABLE_CONTENT =  SERVER_URL + "/api/db/%s/table/%s";

}
