package com.example.myothercatalog;

import android.os.Parcel;
import android.os.Parcelable;

import androidx.annotation.NonNull;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.Serializable;

public class MyItem implements Parcelable {

    private String itemName;  // Nombre del elemento
    private String itemDescription;
    private String imageUrl;   // URL de la imagen del elemento

    // Constructor que recibe un objeto JSON y extrae información para inicializar el objeto MyItem
    public MyItem(JSONObject json) {
        try {
            // Obtiene el nombre del elemento del campo "name" en el objeto JSON
            this.itemName = json.getString("name");
            this.itemDescription = json.getString("description");
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

    public String getItemDescription(){
        return itemDescription;
    }

    // Método para obtener la URL de la imagen del elemento
    public String getImageUrl() {
        return imageUrl;
    }


    // Parcelable
    protected MyItem(Parcel in) {
        itemName = in.readString();
        itemDescription = in.readString();
        imageUrl = in.readString();
    }

    public static final Creator<MyItem> CREATOR = new Creator<MyItem>() {
        @Override
        public MyItem createFromParcel(Parcel in) {
            return new MyItem(in);
        }

        @Override
        public MyItem[] newArray(int size) {
            return new MyItem[size];
        }
    };

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeString(itemName);
        dest.writeString(itemDescription);
        dest.writeString(imageUrl);
    }
}

