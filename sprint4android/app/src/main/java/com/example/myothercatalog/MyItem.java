package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.Serializable;

public class MyItem {

    private String itemName;  // Nombre del elemento
    private String imageUrl;   // URL de la imagen del elemento

    // Constructor que recibe un objeto JSON y extrae información para inicializar el objeto MyItem
    public MyItem(JSONObject json) {
        try {
            // Obtiene el nombre del elemento del campo "name" en el objeto JSON
            this.itemName = json.getString("name");

            // Obtiene la URL de la imagen del campo "image_url" en el objeto JSON
            this.imageUrl = json.getString("image_url");
        } catch (JSONException e) {
            // Maneja la excepción JSONException en caso de errores al analizar el JSON
            e.printStackTrace();
        }
    }

    // Método para obtener el nombre del elemento
    public String getItemName() {
        return itemName;
    }

    // Método para obtener la URL de la imagen del elemento
    public String getImageUrl() {
        return imageUrl;
    }
}

