package com.example.chartexample;

import android.graphics.Color;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.TextView;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import com.github.mikephil.charting.charts.LineChart;
import com.github.mikephil.charting.components.XAxis;
import com.github.mikephil.charting.components.YAxis;
import com.github.mikephil.charting.data.Entry;
import com.github.mikephil.charting.data.LineData;
import com.github.mikephil.charting.data.LineDataSet;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        View textView = findViewById(R.id.textView);

        textView.setOnClickListener(this::createDialog);
    }

    private void createDialog(View view) {
        // 팝업 다이얼로그 생성
        LayoutInflater inflater = getLayoutInflater();
        View dialogView = inflater.inflate(R.layout.custom_dialog_layout, null);

// 다이얼로그 크기 설정
        int width = (int) (getResources().getDisplayMetrics().widthPixels * 0.7);
        int height = (int) (getResources().getDisplayMetrics().heightPixels * 0.6);
        dialogView.setMinimumWidth(width);
        dialogView.setMinimumHeight(height);

// 다이얼로그 뷰 설정
        TextView dialogTitle = dialogView.findViewById(R.id.dialog_title);
        TextView dialogMessage = dialogView.findViewById(R.id.dialog_message);
        LineChart chart = dialogView.findViewById(R.id.chart);

// 데이터 생성
        List<Entry> entries = new ArrayList<>();
        for (int i = 0; i < 100; i++) {
            float x = (float) i;
            float y = (float) Math.log10(x + 1) * 100;
            entries.add(new Entry(x, y));
        }
        LineDataSet dataSet = new LineDataSet(entries, "Log Chart");
        dataSet.setColor(Color.BLACK);
        dataSet.setLineWidth(2f);
        dataSet.setDrawValues(false);
        dataSet.setDrawCircleHole(false);
        dataSet.setDrawCircles(false);

// X 축 설정
        XAxis xAxis = chart.getXAxis();
        xAxis.setPosition(XAxis.XAxisPosition.BOTTOM);
        xAxis.setGranularity(1f);
        xAxis.setDrawGridLines(false);
        xAxis.setAxisLineColor(Color.BLACK);

// Y 축 설정
        YAxis yAxis = chart.getAxisLeft();
        yAxis.setAxisMinimum(0f);
        yAxis.setAxisMaximum(400f);
        yAxis.setGranularity(100f);
        yAxis.setLabelCount(5, true);
        yAxis.setDrawGridLines(true);
        yAxis.setGridColor(Color.LTGRAY);
        yAxis.setAxisLineColor(Color.BLACK);
        YAxis ryAxis = chart.getAxisRight();
        ryAxis.setEnabled(false);

// 차트 설정
        chart.getDescription().setEnabled(false);
        chart.setTouchEnabled(false);
        chart.setDragEnabled(false);
        chart.setScaleEnabled(false);
        chart.setDrawGridBackground(false);
        chart.getLegend().setEnabled(false);
        chart.setData(new LineData(dataSet));
        chart.invalidate();

// 다이얼로그 뷰 적용
        AlertDialog.Builder builder = new AlertDialog.Builder(view.getContext());
        dialogTitle.setText("Dialog Title");
        dialogMessage.setText("Dialog Message");
        builder.setView(dialogView);


// 다이얼로그 표시
        builder.setPositiveButton("확인", null);
        builder.setNegativeButton("취소", null);
        AlertDialog dialog = builder.create();
        dialog.show();
    }
}