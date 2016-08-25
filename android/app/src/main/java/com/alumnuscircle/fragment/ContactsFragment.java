package com.alumnuscircle.fragment;

import android.app.Fragment;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.FragmentManager;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.Toolbar;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.PopupWindow;
import android.widget.TextView;
import android.widget.Toast;

import com.alumnuscircle.R;
import com.alumnuscircle.connections.Adapter.ContactsAdapter;
import com.alumnuscircle.connections.Item.ContactsItem;
import com.alumnuscircle.connections.ItemDecrotion.DividerItemDecoration;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by 曾博晖 on 2016/8/22.
 * 人脉界面碎片
 * @author 曾博晖
 */
public class ContactsFragment extends Fragment implements View.OnClickListener{
//    private TextView textView_toolbar;
    private Toolbar toolbar;
    private ImageButton btn_search;
    private ImageButton btn_filter;
    private RecyclerView recyclerView_contacts;
    private List<ContactsItem> mDatas;
    private ContactsAdapter mAdapter;
    private PopupWindow popupWindow;
    private Button btn_filterOk;
    private Button btn_clearFilter;
    private Button btn_highlyFilter;
    private Button btn_check1;
    private Button btn_check2;
    private Button btn_check3;
    private Boolean IsBox1Selected;
    private Boolean IsBox2Selected;
    private Boolean IsBox3Selected;
    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view=inflater.inflate(R.layout.fragment_contacts,container,false);
        initView(view);
        initData();
        initRecycleView();
        return view;
    }
    /**
     * 向RecycleView里面添加数据
     * 曾博晖
     * 2016年8月23日17:37:12
     * 创建*/
    private void initRecycleView() {
        recyclerView_contacts.setLayoutManager(new LinearLayoutManager(getActivity()));
        recyclerView_contacts.setAdapter(mAdapter = new ContactsAdapter(getActivity(),mDatas));
        recyclerView_contacts.addItemDecoration(new DividerItemDecoration(getActivity(),
                DividerItemDecoration.VERTICAL_LIST));
    }

    /**
     * 加载用户数据
     * 曾博晖
     * 2016年8月23日17:25:33
     * 创建
     * */
    private void initData() {
        mDatas = new ArrayList<>();
        ContactsItem contect1=new ContactsItem(
                "http://img2.imgtn.bdimg.com/it/u=3413454958,4293050372&fm=11&gp=0.jpg",
                "赵小雨","南京","艺术学院2012级","工业设计1班",
                "彩妆师"
        );
        ContactsItem contect2=new ContactsItem(
                "http://v1.qzone.cc/avatar/201508/30/00/39/55e1e026dc781749.jpg%21200x200.jpg",
                "李崇","苏州","信息学院2012级","电子电路4班",
                "软件工程师"
        );
        ContactsItem contect3=new ContactsItem(
                "http://img2.imgtn.bdimg.com/it/u=3529368069,13239119&fm=21&gp=0.jpg",
                "苏小陌","杭州","经管学院2012级","投资路4班",
                "高级理财师"
        );
        mDatas.add(contect1);
        mDatas.add(contect2);
        mDatas.add(contect3);

    }

    /**
     * 初始化人脉界面
     * 2016年8月23日15:21:48 曾博晖
     * 创建*/
    private void initView(View view){
        toolbar=(Toolbar)view.findViewById(R.id.toolbar);
        toolbar.setTitle("");
        btn_search=(ImageButton)view.findViewById(R.id.search_btn);
        btn_search.setOnClickListener(this);
        btn_filter=(ImageButton)view.findViewById(R.id.filter_btn);
        btn_filter.setOnClickListener(this);
        recyclerView_contacts=(RecyclerView)view.findViewById(R.id.recView_contacts);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.search_btn:
                Toast.makeText(getActivity(),"查找人脉",
                        Toast.LENGTH_SHORT).show();
                break;
            case R.id.filter_btn:
                Toast.makeText(getActivity(),"筛选人脉",
                        Toast.LENGTH_SHORT).show();
                showPopWindow();
                break;
            case R.id.checkbox1:
                IsBox1Selected=true;
                btn_check1.setBackgroundResource(R.mipmap.checkbox_ok);
            break;
            case R.id.checkbox2:
                IsBox2Selected=true;
                btn_check2.setBackgroundResource(R.mipmap.checkbox_ok);
                break;
            case R.id.checkbox3:
                IsBox3Selected=true;
                btn_check3.setBackgroundResource(R.mipmap.checkbox_ok);
                break;
            case R.id.btn_filterOK:
                Toast.makeText(getActivity(),"开始筛选",Toast.LENGTH_SHORT).show();
                popupWindow.dismiss();
                break;
            case R.id.btn_clearFilter:
                initCheckBox();
                break;
            case R.id.btn_highlyFilter:
                //跳转到高级筛选界面
                popupWindow.dismiss();
            default:
                break;
        }

    }
    /**
     * 显示PopupWindow
     * 曾博晖
     * 2016年8月24日11:26:16
     * 创建
     * */
    private void showPopWindow() {
        //设置contentView
        View contentView = LayoutInflater.from(getActivity()).inflate(R.layout.popupwindow_filter, null);
        popupWindow = new PopupWindow(contentView,
                ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT, true);
        popupWindow.setContentView(contentView);
        initPopView(contentView);
        //显示PopupWindow
        View rootview = LayoutInflater.from(getActivity()).inflate(R.layout.fragment_contacts, null);
        popupWindow.showAtLocation(rootview, Gravity.TOP, 0,100);
    }
    private void initPopView (View contentView)
    {
        btn_check1=(Button)contentView.findViewById(R.id.checkbox1);
        btn_filterOk=(Button)contentView.findViewById(R.id.btn_filterOK);
        btn_check2=(Button)contentView.findViewById(R.id.checkbox2);
        btn_check3=(Button)contentView.findViewById(R.id.checkbox3);
        btn_clearFilter=(Button)contentView.findViewById(R.id.btn_clearFilter);
        btn_highlyFilter=(Button)contentView.findViewById(R.id.btn_highlyFilter);
        btn_clearFilter.setOnClickListener(this);
        btn_highlyFilter.setOnClickListener(this);
        btn_check3.setOnClickListener(this);
        btn_check2.setOnClickListener(this);
        btn_check1.setOnClickListener(this);
        btn_filterOk.setOnClickListener(this);
        initCheckBox();
    }
    /**
     * 将各个选项前的选框改为未选
     * */
    private void initCheckBox(){
        btn_check1.setBackgroundResource(R.mipmap.checkbox);
        btn_check2.setBackgroundResource(R.mipmap.checkbox);
        btn_check3.setBackgroundResource(R.mipmap.checkbox);
    }
}
