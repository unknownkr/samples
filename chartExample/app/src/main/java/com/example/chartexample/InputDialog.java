package com.example.chartexample;

import android.app.Dialog;
import android.content.Context;
import android.widget.Button;
import android.widget.EditText;

import androidx.annotation.NonNull;

public class InputDialog extends Dialog {
    private final EditText input;

    public interface InputDialogListener {
        void OnClickListener(int data);
    }

    public InputDialog(@NonNull Context context, InputDialogListener listener) {
        super(context);

        setContentView(R.layout.input_dialog);

        int width = (int) (context.getResources().getDisplayMetrics().widthPixels * 0.8);
        int height = (int) (context.getResources().getDisplayMetrics().heightPixels * 0.4);
        getWindow().setLayout(width, height);

        input = findViewById(R.id.input);
        Button shutdownClick = findViewById(R.id.btn_ok);
        shutdownClick.setOnClickListener(v -> {
            String inputText = input.getText().toString();
            if (!inputText.isEmpty()) {
                listener.OnClickListener(Integer.parseInt(inputText));
            }
            dismiss();
        });

    }
}
