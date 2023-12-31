package com.example.myothercatalog;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    // Declaración de variables miembro
    private RecyclerView recyclerView;   // RecyclerView para mostrar la lista de elementos
    private MyAdapter adapter;           // Adaptador personalizado para el RecyclerView
    private ArrayList<MyItem> itemList;  // Lista de elementos que se mostrarán en el RecyclerView
    private String catalogUrl = "https://raw.githubusercontent.com/beisss/DI/main/resources/catalog.json";

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        // Llama al método onCreate de la clase base (AppCompatActivity)
        super.onCreate(savedInstanceState);
        // Establece el diseño de la interfaz de usuario asociado con esta actividad
        setContentView(R.layout.activity_main);

        // Inicialización del RecyclerView y otras variables
        recyclerView = findViewById(R.id.recyclerView);  // Busca el RecyclerView en el diseño
        Activity activity = this;  // Referencia a la actividad actual para usar en las callbacks

        // Creación de una solicitud JSON para obtener datos del catálogo
        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                catalogUrl,
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        // Maneja la respuesta exitosa del servidor

                        List<MyItem> allThePokemon = new ArrayList<>();  // Lista para almacenar elementos

                        // Itera a través del JSONArray para obtener datos de cada elemento
                        for (int i = 0; i < response.length(); i++) {
                            try {
                                // Obtiene un objeto JSON que representa un elemento del catálogo
                                JSONObject pokemon = response.getJSONObject(i);
                                MyItem data = new MyItem(pokemon);  // Crea un objeto MyItem a partir del JSONObject
                                allThePokemon.add(data);  // Agrega el objeto a la lista
                            } catch (JSONException e) {
                                e.printStackTrace();
                            }
                        }

                        // Crea un nuevo adaptador y configura el RecyclerView
                        MyAdapter adapter = new MyAdapter(allThePokemon, activity);
                        recyclerView.setAdapter(adapter);  // Asigna el adaptador al RecyclerView
                        recyclerView.setLayoutManager(new LinearLayoutManager(activity));  // Configura el diseño del RecyclerView

                        // Establece un Listener de clics para los elementos del RecyclerView
                        adapter.setOnItemClickListener(new MyAdapter.OnItemClickListener() {
                            @Override
                            public void onItemClick(int position) {
                                try {
                                    // Obtiene el objeto MyItem correspondiente a la posición seleccionada
                                    MyItem pokemonClicked = allThePokemon.get(position);

                                    // Crea un Intent para abrir la actividad DetailActivity
                                    Intent intent = new Intent(MainActivity.this, DetailActivity.class);

                                    // Agrega el objeto MyItem como extra al Intent con la clave "pokemon"
                                    intent.putExtra("pokemon", pokemonClicked);

                                    // Inicia la actividad DetailActivity
                                    startActivity(intent);
                                } catch (Exception e) {
                                    // Captura y registra cualquier excepción que ocurra al abrir DetailActivity
                                    e.printStackTrace();
                                    Log.e("TAG", "Error al abrir DetailActivity: " + e.getMessage());
                                }
                            }
                        });

                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // Maneja errores en la solicitud y muestra un mensaje Toast
                        Toast.makeText(activity, error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                });

        // Creación y ejecución de la cola de solicitudes Volley
        RequestQueue cola = Volley.newRequestQueue(this);
        cola.add(request);  // Agrega la solicitud a la cola para su procesamiento
    }
}
