package com.example.mycatalog;

import androidx.annotation.NonNull;
import androidx.annotation.StringRes;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;

import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.Toast;

import com.google.android.material.navigation.NavigationView;

public class HomeActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener {
    private DrawerLayout drawerLayout;
    private NavigationView navigationView;
    private MenuItem catalogItem;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        // Configurar la barra de herramientas como la barra de acción
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        // Inicializar el DrawerLayout y el ActionBarDrawerToggle para el menú desplegable
        drawerLayout = findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawerLayout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawerLayout.addDrawerListener(toggle);
        toggle.syncState();

        // Inicializar el NavigationView y establecer el escuchador para los elementos de menú
        navigationView = findViewById(R.id.navigation_view);
        navigationView.setNavigationItemSelectedListener(this);

        // Configurar un clic en el título del encabezado para mostrar un mensaje Toast
        View header = navigationView.getHeaderView(0);
        header.findViewById(R.id.header_title).setOnClickListener(view -> Toast.makeText(
                HomeActivity.this,
                getString(R.string.title_click),
                Toast.LENGTH_SHORT).show()
        );

        // Obtener el elemento de menú "Catalog" y marcarlo como seleccionado
        catalogItem = navigationView.getMenu().getItem(0).getSubMenu().getItem(0);
        onNavigationItemSelected(catalogItem);
        catalogItem.setChecked(true);
    }

    @Override
    public void onBackPressed() {
        // Manejar el botón Atrás para cerrar el menú desplegable si está abierto
        if (drawerLayout.isDrawerOpen(GravityCompat.START)) {
            drawerLayout.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem menuItem) {
        // Manejar la selección de elementos de menú en el NavigationView
        if (menuItem.getItemId() != R.id.nav_catalog)
            catalogItem.setChecked(false);
        showFragment(getTitle(menuItem));
        drawerLayout.closeDrawer(GravityCompat.START);
        return true;
    }

    private int getTitle(@NonNull MenuItem menuItem) {
        // Obtener el título del elemento de menú y devolver su identificador de cadena
        String nombre = String.valueOf(menuItem.getTitle());
        switch (nombre) {
            case "Catalog":
                return R.string.menu_catalog;
            case "About":
                return R.string.menu_about;
            default:
                throw new IllegalArgumentException("That option isn't implemented!!");
        }
    }

    private void showFragment(@StringRes int titleId) {
        // Mostrar un fragmento correspondiente al elemento de menú seleccionado
        if (titleId == R.string.menu_catalog) {
            Fragment fragment = FragmentCatalog.newInstance(titleId);
            getSupportFragmentManager()
                    .beginTransaction()
                    .replace(R.id.home_content, fragment)
                    .commit();
            setTitle(getString(titleId));
        } else if (titleId == R.string.menu_about) {
            Fragment fragment = FragmentAbout.newInstance(titleId);
            getSupportFragmentManager()
                    .beginTransaction()
                    .replace(R.id.home_content, fragment)
                    .commit();
            setTitle(getString(titleId));
        }
    }
}
