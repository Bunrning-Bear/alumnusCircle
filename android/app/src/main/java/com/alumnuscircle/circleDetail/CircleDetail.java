package com.alumnuscircle.circleDetail;

import android.app.Activity;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.alumnuscircle.R;

/**
 * Created by 15359 on 2016/8/25.
 * 圈子详情界面
 */
public class CircleDetail extends AppCompatActivity {

    private ImageView float_button;
    private Button edit,chat,share,exit,search,setting,back,invite;
    private Toolbar toolbar;
    private  LinearLayout redBg;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.detail);
     InitView();

    }



    /**
     * 隐藏toolbar图标
     */
    private  void HideToolbar()
    {
        TextView tv =(TextView)findViewById(R.id.detail_tvback);
        tv.setVisibility(View.GONE);
        search.setVisibility(View.GONE);
        setting.setVisibility(View.GONE);
        back.setVisibility(View.GONE);
    }

    /**
     * 显示toolbar图标
     */
   private void ShowToolbar()
   {
       TextView tv =(TextView)findViewById(R.id.detail_tvback);
       tv.setVisibility(View.VISIBLE);
       search.setVisibility(View.VISIBLE);
       setting.setVisibility(View.VISIBLE);
       back.setVisibility(View.VISIBLE);
   }
    /**
     * 初始化界面
     */
    private void InitView()
    {
        //初始化

        toolbar = (Toolbar) findViewById(R.id.detailTb);
        setSupportActionBar(toolbar);
        float_button = (ImageView)findViewById(R.id.detail_float);
        invite = (Button)findViewById(R.id.detail_invite);
        search = (Button)findViewById(R.id.detail_search);
        setting = (Button)findViewById(R.id.deatil_setting);
        edit=(Button)findViewById(R.id.deatil_edit);
        chat=(Button)findViewById(R.id.deatil_chat);
        share=(Button)findViewById(R.id.deatil_share);
        exit=(Button)findViewById(R.id.deatil_exit);
        back = (Button)findViewById(R.id.detail_back);
        redBg = (LinearLayout)findViewById(R.id.redBg);


        //监听
        float_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                redBg.setFocusable(true);
                redBg.setVisibility(View.VISIBLE);
                //隐藏浮动按钮
                float_button.setVisibility(View.GONE);
                float_button.setFocusable(false);
                //隐藏toolbar
               HideToolbar();

            }
        });

        exit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                redBg.setFocusable(false);
                redBg.setVisibility(View.GONE);
                //显示浮动按钮
                float_button.setVisibility(View.VISIBLE);
                float_button.setFocusable(true);
                //显示toolbar
               ShowToolbar();
            }


        });
        chat.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(CircleDetail.this,"这是聊天",Toast.LENGTH_SHORT).show();
            }
        });

        setting.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(CircleDetail.this,"这是设置",Toast.LENGTH_SHORT).show();
            }
        });
        search.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(CircleDetail.this,"搜索",Toast.LENGTH_SHORT).show();
            }
        });
        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });
    }
}
