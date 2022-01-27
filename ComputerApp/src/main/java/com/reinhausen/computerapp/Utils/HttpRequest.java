package com.reinhausen.computerapp.Utils;

import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

public class HttpRequest {

    // one instance, reuse
    private final HttpClient HTTP_CLIENT = HttpClient.newBuilder().version(HttpClient.Version.HTTP_2).build();

    private final String request_url;
    private final String request_method;
    private final String USER_AGENT;
    private String RETURNED_REQUEST = "";
    private HttpResponse<String> HTTP_REPONSE;

    public HttpRequest(String url, String method){
        this.USER_AGENT = "c-app";

        this.request_url = url;
        this.request_method = method;

        if (this.request_method.toUpperCase().equals("POST")){
            this.Post();
        }else if (this.request_method.toUpperCase().equals("GET")){
            this.Get();
        }
    }



    public String GetReponse(){
        return this.RETURNED_REQUEST;
    }

    public String GetHttpReponse(){
        return this.HTTP_REPONSE.toString();
    }



   public String Get(){
       try {
           java.net.http.HttpRequest request = java.net.http.HttpRequest.newBuilder().GET()
                   .uri(URI.create(this.request_url))
                   .setHeader("User-Agent", USER_AGENT)
                   .build();

           HttpResponse<String> response = HTTP_CLIENT.send(request, HttpResponse.BodyHandlers.ofString());

           return response.body();
       } catch (Exception e) {
            e.printStackTrace();
        }
       return null;
   }

    public String Post() {
        try {
            // post data
            Map<Object, Object> data = new HashMap<>();
            // data.put("username", "abc");

            java.net.http.HttpRequest request = java.net.http.HttpRequest.newBuilder().POST(buildGetRequestParams(data))
                    .uri(URI.create(this.request_url))
                    .setHeader("User-Agent", USER_AGENT) // add request header
                    .header("Content-Type", "application/json")
                    .build();

            try{
                this.HTTP_REPONSE = this.HTTP_CLIENT.send(request, HttpResponse.BodyHandlers.ofString());
                this.RETURNED_REQUEST = this.HTTP_REPONSE.body();
            }catch (Exception e){
                this.RETURNED_REQUEST = "Couldn't execute POST Request";
            }

        } catch (Exception e) {
            e.printStackTrace();
            this.RETURNED_REQUEST = e.toString();
        }
        return this.RETURNED_REQUEST;

    }



    public static java.net.http.HttpRequest.BodyPublisher buildGetRequestParams(Map<Object, Object> data) {
        var builder = new StringBuilder();
        for (Map.Entry<Object, Object> entry : data.entrySet()) {
            if (builder.length() > 0) {
                builder.append("&");
            }
            builder.append(URLEncoder.encode(entry.getKey().toString(), StandardCharsets.UTF_8));
            builder.append("=");
            builder.append(URLEncoder.encode(entry.getValue().toString(), StandardCharsets.UTF_8));
        }
        System.out.println(builder.toString());
        return java.net.http.HttpRequest.BodyPublishers.ofString(builder.toString());
    }
}


