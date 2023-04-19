package com.example.scopestorage;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.provider.Settings;
import android.util.Log;
import android.view.View;

import com.google.android.material.snackbar.Snackbar;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.ByteBuffer;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
            if (!Environment.isExternalStorageManager()) {
                Snackbar.make(findViewById(android.R.id.content), "Permission needed!", Snackbar.LENGTH_INDEFINITE).setAction("Settings", new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        try {
                            Uri uri = Uri.parse("package:${BuildConfig.APPLICATION_ID}");
                            Intent intent = new Intent(Settings.ACTION_MANAGE_APP_ALL_FILES_ACCESS_PERMISSION, uri);
                            startActivity(intent);
                        } catch (Exception ex) {
                            Intent intent = new Intent();
                            intent.setAction(Settings.ACTION_MANAGE_ALL_FILES_ACCESS_PERMISSION);
                            startActivity(intent);
                        }
                    }
                }).show();
            }
        }

        // File write app directory
        File appDir = getExternalFilesDir(Environment.DIRECTORY_DOCUMENTS + "/mydir/");
        String filename = "app_file.txt";
        File appFilePath = new File(appDir, filename);
        if (!appDir.exists()) {
            boolean mkdir = appDir.mkdir();
            Log.i("main", "app mkdir: " + mkdir);
        }
        try (FileOutputStream fos = new FileOutputStream(appFilePath)) {
            fos.write("TEST WRITE TO APP DIR\n".getBytes());
            fos.flush();
            Log.i("main", "app_file.txt write finished\n");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        // File write external directory
        File externalDir = new File(Environment.getExternalStorageDirectory() + "/Test/");
        String filename2 = "test2.txt";
        File externalPath = new File(externalDir, filename2);
        if (!externalDir.exists()) {
            boolean mkdir = externalDir.mkdir();
            Log.i("main", "ext mkdir: " + mkdir);
        }
        try (FileOutputStream fos = new FileOutputStream(externalPath)) {
            fos.write("TEST WRITE TO external DIR".getBytes());
            fos.flush();
            Log.i("main", "test2.txt write finished\n");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}