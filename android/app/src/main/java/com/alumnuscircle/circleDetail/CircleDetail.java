package com.alumnuscircle.circleDetail;

import android.app.Activity;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;

import com.alumnuscircle.R;

/**
 * Created by 15359 on 2016/8/25.
 * 圈子详情界面
 */
public class CircleDetail extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.detail);
        Toolbar toolbar =(Toolbar)findViewById(R.id.detailTb);
        setSupportActionBar(toolbar);

    }
}
