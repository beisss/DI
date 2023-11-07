package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class CatalogActivity extends AppCompatActivity {
    private Button button1;
    private Context context;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Establecer la vista asociada a esta actividad desde el archivo XML "activity_catalog.xml"
        setContentView(R.layout.activity_catalog);

        // Obtener una referencia al botón con ID "button1" en el diseño
        button1 = findViewById(R.id.button1);
        context = this;

        // Establecer un listener para el botón "button1" que escucha el evento de clic
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Crear un intent para abrir la actividad "DetailActivity"
                Intent intent = new Intent(context, DetailActivity.class);
                // Iniciar la actividad "DetailActivity"
                startActivity(intent);
            }
        });
    }
}