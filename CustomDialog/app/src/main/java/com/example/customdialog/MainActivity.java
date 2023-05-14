package com.example.customdialog;

import android.app.AlertDialog;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        findViewById(R.id.button).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
//                CustomDialog customDialog = new CustomDialog(MainActivity.this);

                LayoutInflater inflater = getLayoutInflater();
                View v = inflater.inflate(R.layout.dialog, null);
                AlertDialog.Builder builder = new AlertDialog.Builder(MainActivity.this);
                builder.setView(v);
                builder.setPositiveButton("OK", (dialogInterface, i) -> {
                });
                builder.create();
                builder.show();
            }
        });

    }
}