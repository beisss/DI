package com.example.myothercatalog;

import android.os.Bundle;
import android.util.Log;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;

public class DetailActivity extends AppCompatActivity {
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        // Obtener la información del animal del intent
        MyItem pokemon = getIntent().getParcelableExtra("pokemon");

        // Referencias a los elementos de la interfaz de usuario en activity_detail.xml
        ImageView imageView = findViewById(R.id.pokeImage2);
        TextView textTitle = findViewById(R.id.pokeTitle);
        TextView textDescription = findViewById(R.id.pokeDescription);

        if (pokemon != null) {
            textTitle.setText(pokemon.getItemName());
            textDescription.setText(pokemon.getItemDescription());

            Glide.with(this)
                    .load(pokemon.getImageUrl())
                    .into(imageView);
        } else {
            Log.e("TAG", "Objeto MyItem es nulo en DetailActivity");
        }
    }
}
