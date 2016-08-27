package com.alumnuscircle.connections.Activity;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.alumnuscircle.R;
import com.alumnuscircle.connections.Adapter.BitmapCache;
import com.alumnuscircle.connections.Image.CircleNetworkImage;
import com.android.volley.RequestQueue;
import com.android.volley.toolbox.ImageLoader;
import com.android.volley.toolbox.NetworkImageView;
import com.android.volley.toolbox.Volley;

/**
 * Created by 曾博晖 on 2016/8/26.
 * 人脉详情界面
 * @author 曾博晖
 */

public class particularActivity extends AppCompatActivity implements View.OnClickListener {
    private NetworkImageView headImg_bottom;
    private CircleNetworkImage headImg_Top;

    private TextView userName;
    private TextView userJobTitle;
    private TextView userLocation;
    private TextView userSchool;
    private TextView userDepartment;
    private TextView userClass;
    private TextView userEduStartDate;
    private TextView userCompany;
    private TextView userVocation;

    private String headImgUrl;

    //下面的都是可以监听事件的
    private Button btn_leaveMsg;
    private Button btn_back;
    private LinearLayout dynamicLayout;
    private LinearLayout collectLayout;
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState)  {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_contactsparticulars);
        initWidget();
        initView();

    }
    /**
     * 初始化空间列表
     * 2016年8月26日14:43:14
     * 曾博晖
     * 创建
     * */
    private void initWidget(){
        headImg_bottom=(NetworkImageView)findViewById(R.id.ptcActivity_headImgBottom);
        headImg_Top=(CircleNetworkImage)findViewById(R.id.ptcActivity_headImgTop);

        userName=(TextView)findViewById(R.id.pctActivityName_tv);
        userJobTitle=(TextView)findViewById(R.id.pctActivityJobTitle_tv);
        userLocation=(TextView)findViewById(R.id.pctActivityLocation_tv);
        userSchool=(TextView)findViewById(R.id.pctActivity_tvSchool);
        userDepartment=(TextView)findViewById(R.id.pctActivity_tvDepartment);
        userClass=(TextView)findViewById(R.id.pctActivity_tvClass);
        userEduStartDate=(TextView)findViewById(R.id.pctActivity_tvEduStartDate);
        userCompany=(TextView)findViewById(R.id.pctActivity_tvCompany);
        userVocation=(TextView)findViewById(R.id.pctActivity_tvVocation);

        btn_back=(Button)findViewById(R.id.ptcActivity_btn_back);
        btn_leaveMsg=(Button)findViewById(R.id.pctActivityBtn_leaveMsg);
        collectLayout=(LinearLayout)findViewById(R.id.ptcActivity_collectLayout);
        dynamicLayout=(LinearLayout)findViewById(R.id.pctActivity_dynamicLayout);
    }
    /**
     * 初始化界面，接收上个界面传来的数据
     * 曾博晖 2016年8月26日14:55:08
     * 创建
     * */
    private void initView(){
        Bundle bundle=getIntent().getExtras();
        headImgUrl=bundle.getString("headImgUrl");
        Load_HeadPortrait(headImg_bottom,headImgUrl);
        Load_HeadPortrait(headImg_Top,headImgUrl);
        userName.setText(bundle.getString("name"));
        userDepartment.setText(bundle.getString("department"));
        userJobTitle.setText(bundle.getString("job"));
        userClass.setText(bundle.getString("class"));
        userEduStartDate.setText(bundle.getString("grade"));
        userLocation.setText(bundle.getString("location"));

        btn_back.setOnClickListener(this);
        btn_leaveMsg.setOnClickListener(this);
        dynamicLayout.setOnClickListener(this);
        collectLayout.setOnClickListener(this);
    }
    /**
     * 利用Volley的Http请求进行加载头像的操作
     * 曾博晖
     * 2016年8月6日 创建
     * */
    public void Load_HeadPortrait(NetworkImageView networkImageView,String img_url) {
        RequestQueue mQueue = Volley.newRequestQueue(particularActivity.this);//申请一个队列
        ImageLoader imageLoader = new ImageLoader(mQueue, new BitmapCache() {
        });
        networkImageView.setErrorImageResId(R.mipmap.ic_launcher);
        networkImageView.setImageUrl(img_url,imageLoader);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.ptcActivity_btn_back:
                finish();
                break;
            case R.id.pctActivity_dynamicLayout:
                //跳转到动态界面
                Toast.makeText(this,"展开到动态",Toast.LENGTH_SHORT).show();
                break;
            case R.id.ptcActivity_collectLayout:
                Toast.makeText(this,"收藏"+userName.getText().toString()
                        +"的名片！",Toast.LENGTH_SHORT).show();
                break;
            case R.id.pctActivityBtn_leaveMsg:
                Toast.makeText(this,"将对"+userName.getText().toString()
                        +"进行留言",Toast.LENGTH_SHORT).show();
                break;
            default:
                break;
        }
    }
}
