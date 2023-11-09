package com.example.mycatalog;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.annotation.Nullable;
import androidx.annotation.StringRes;
import androidx.fragment.app.Fragment;

public class FragmentCatalog extends Fragment {
    private Button button;
    private Context context;

    // Método estático para crear una nueva instancia del fragmento con un ID de texto
    public static FragmentCatalog newInstance(@StringRes int textId) {
        FragmentCatalog frag = new FragmentCatalog();
        return frag;
    }

    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        // Inflar el diseño del fragmento "fragment_catalog.xml" en la vista
        View layout = inflater.inflate(R.layout.fragment_catalog, container, false);

        // Obtener una referencia al botón con ID "button1" en el diseño
        button = layout.findViewById(R.id.button1);

        // Establecer un listener para el botón que abre la actividad "DetailActivity" al hacer clic
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Crear un intent para abrir la actividad "DetailActivity"
                Intent intentDetailActivity = new Intent(context, DetailActivity.class);
                startActivity(intentDetailActivity);
            }
        });

        return layout; // Devolver la vista inflada como la vista del fragmento
    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        this.context = context;
    }
}
