package com.example.customdialog;

import android.app.Dialog;
import android.content.Context;
import android.view.View;
import android.widget.Button;

import androidx.annotation.NonNull;

public class CustomDialog extends Dialog {
    private Button positive, negative;

    public CustomDialog(@NonNull Context context) {
        super(context);
        setContentView(R.layout.dialog);
    }

    public void setPositiveButton(String buttonText, View.OnClickListener listener) {
        positive.setText(buttonText);
        positive.setOnClickListener(listener);
        positive.setVisibility(View.VISIBLE);
    }
}
