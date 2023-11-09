package com.example.mycatalog;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.Nullable;
import androidx.annotation.StringRes;
import androidx.fragment.app.Fragment;

public class FragmentAbout extends Fragment {

    // Método estático para crear una nueva instancia del fragmento con un ID de texto
    public static FragmentAbout newInstance(@StringRes int textId) {
        FragmentAbout frag = new FragmentAbout();
        return frag;
    }

    // Método que se llama cuando se crea la vista del fragmento
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        // Inflar el diseño del fragmento "fragment_about.xml" en la vista
        View layout = inflater.inflate(R.layout.fragment_about, container, false);

        return layout; // Devolver la vista inflada como la vista del fragmento
    }
}
