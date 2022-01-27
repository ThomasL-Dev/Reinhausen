package com.reinhausen.computerapp.Utils;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class HttpReponse {

    private static String BASE_REPONSE;
    private static List<String> DATA = new ArrayList<String>();

    private String IP;
    private String METHOD;
    private String LOC;
    private String URI;
    private String REPONSE;

    public HttpReponse(String reponse) {
        BASE_REPONSE = reponse;
        this.SortReqValues();

        System.out.println("REQUEST {");

        this.IP = String.valueOf(this.GetIpFromDict());
        System.out.println("\tIp : " + this.IP);

        this.METHOD = String.valueOf(this.GetMethodFromDict());
        System.out.println("\tMethod : " + this.METHOD);

        this.LOC = String.valueOf(this.GetLocFromDict());
        System.out.println("\tLoc : " + this.LOC);

        this.URI = String.valueOf(this.GetUriFromDict());
        System.out.println("\tUri : " + this.URI);

        this.REPONSE = String.valueOf(this.GetReponseFromDict());
        System.out.println("\tReponse : " + this.REPONSE);
        System.out.println("}");
        DATA.clear();

    }



    public String GetMethod() {
        return this.METHOD;
    }

    public String GetUri() {
        return this.URI;
    }

    public String GetIp() {
        return this.IP;
    }

    public String GetLoc() {
        return this.LOC;
    }

    public String GetReponse() {
        return this.REPONSE;
    }




    protected String GetMethodFromDict() {
        try {
            return DATA.get(2);
        }catch (Exception e){
            return "Null";
        }
    }

    protected String GetUriFromDict() {
        try {
            return DATA.get(4);
        }catch (Exception e){
            return "Null";
        }
    }

    protected String GetIpFromDict() {
        try {
            return DATA.get(6);
        }catch (Exception e){
            return "Null";
        }
    }

    protected String GetLocFromDict() {
        try {
            return DATA.get(8);
        }catch (Exception e){
            return "Null";
        }
    }

    protected String GetReponseFromDict() {
        try{
            for (Integer i = 0; i < 10; i++) {
                try {
                    DATA.remove(0);
                }catch (Exception e){
                    return "Null";
                }
            }
            return DATA.toString().replace(", ", " : ").replace("[", "").replace("]", "");
        }catch (Exception e){
            return "Null";
        }
    }

    protected void SortReqValues() {
        Pattern p = Pattern.compile("\"([^\"]*)\"");
        Matcher m = p.matcher(BASE_REPONSE);
        while (m.find()) {
            DATA.add(m.group(1));
        }
    }
}
