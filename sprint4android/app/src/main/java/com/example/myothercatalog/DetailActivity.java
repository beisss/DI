package com.example.myothercatalog;

import android.os.Bundle;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class DetailActivity extends AppCompatActivity {
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        // Muestra un mensaje provisional Toast indicando que la actividad Detail se ha iniciado con éxito
        Toast.makeText(this, "Activity Detail iniciado con éxito.", Toast.LENGTH_SHORT).show();
    }
}
