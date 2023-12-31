package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class MyAdapter extends RecyclerView.Adapter<MyViewHolder> {

    private List<MyItem> itemList;  // Lista de elementos a mostrar en el RecyclerView
    private Activity activity;      // Referencia a la actividad que utiliza este adaptador
    private OnItemClickListener mListener;  // Interfaz para manejar clics en elementos del RecyclerView

    // Constructor que recibe la lista de elementos y la actividad asociada
    public MyAdapter(List<MyItem> itemList, Activity activity) {
        this.itemList = itemList;
        this.activity = activity;
    }

    // Método llamado cuando se necesita crear un nuevo ViewHolder
    @NonNull
    @Override
    public MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        // Infla el diseño de cada elemento de la lista
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.item_layout, parent, false);
        return new MyViewHolder(view);  // Esta línea invoca el constructor del ViewHolder
    }

    // Método llamado cuando se debe asociar un ViewHolder a un elemento específico en la lista
    @Override
    public void onBindViewHolder(MyViewHolder holder, int position) {
        MyItem myItem = itemList.get(position);
        holder.showData(myItem, activity);  // Llama al método showData del ViewHolder para mostrar los datos
        final int adapterPosition = holder.getAdapterPosition();

        // Configura un OnClickListener para el elemento del RecyclerView
        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Verifica si hay un Listener y la posición del adaptador es válida
                if (mListener != null && adapterPosition != RecyclerView.NO_POSITION) {
                    mListener.onItemClick(adapterPosition); // Llama al método onItemClick del Listener
                }
            }
        });
    }

    // Método que devuelve la cantidad total de elementos en la lista
    @Override
    public int getItemCount() {
        return itemList.size();
    }

    // Interfaz para manejar clics en elementos del RecyclerView
    public interface OnItemClickListener {
        void onItemClick(int position);
    }

    // Método para establecer el Listener para los clics en elementos del RecyclerView
    public void setOnItemClickListener(OnItemClickListener listener) {
        mListener = listener;
    }

}

