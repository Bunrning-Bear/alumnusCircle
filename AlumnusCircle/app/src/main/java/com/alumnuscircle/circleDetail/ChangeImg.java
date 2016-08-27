package com.alumnuscircle.circleDetail;


import android.app.Activity;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.FrameLayout;
import android.widget.ImageButton;
import android.widget.TextView;

import com.alumnuscircle.R;
import com.facebook.drawee.view.SimpleDraweeView;

public class ChangeImg extends Activity {

    private ImageButton ccdtl_chgimg_back_btn;
    private ImageButton ccdtl_chgimg_change_btn;
    private SimpleDraweeView ccdtl_chgimg_headimg;
    private EditText ccdtl_chgimg_name_tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.ccdtl_changeimg);
        init();
    }

    private void init(){
        initUI();
        initData();
    }

    private void initUI(){
        ccdtl_chgimg_back_btn = (ImageButton)findViewById(R.id.ccdtl_chgimg_back_btn);
        ccdtl_chgimg_change_btn = (ImageButton)findViewById(R.id.ccdtl_chgimg_change_btn);
        ccdtl_chgimg_headimg = (SimpleDraweeView)findViewById(R.id.ccdtl_chgimg_headimg);
        ccdtl_chgimg_name_tv = (EditText)findViewById(R.id.ccdtl_chgimg_name_tv);

        ccdtl_chgimg_back_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });

        ccdtl_chgimg_change_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            }
        });
    }

    private void initData(){
        ccdtl_chgimg_name_tv.setText("软件圈");
        ccdtl_chgimg_headimg.setImageURI(Uri.parse("http://f.hiphotos.baidu.com/zhidao/wh%3D600%2C800/sign=39af5230eaf81a4c2667e4cfe71a4c61/3812b31bb051f819b384e30edbb44aed2f73e7d5.jpg"));
    }


}
