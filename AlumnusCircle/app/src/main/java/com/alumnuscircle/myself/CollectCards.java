package com.alumnuscircle.myself;


import android.app.Fragment;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.Toolbar;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageButton;

import com.alumnuscircle.R;
import com.alumnuscircle.connections.Adapter.ContactsAdapter;
import com.alumnuscircle.connections.Item.ContactsItem;

import java.util.ArrayList;
import java.util.List;

public class CollectCards extends Fragment {

    private View view;
    private LayoutInflater layoutInflater;
    private ViewGroup container;

    private RecyclerView rvCollectCards;
    private List<ContactsItem> data;
    private ContactsAdapter adapter;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        view = inflater.inflate(R.layout.me_collect_cards, container, false);
        layoutInflater = inflater;
        this.container = container;
        initView(view);
        initData();
        initRecycleView();
        return view;
    }

    private void initRecycleView() {
        rvCollectCards.setLayoutManager(new LinearLayoutManager(getActivity()));
        rvCollectCards.setAdapter(adapter = new ContactsAdapter(getActivity(),data));

        /**
         * 改成用ImageView
         */
//        recyclerView_contacts.addItemDecoration(new DividerItemDecoration(getActivity(),
//                DividerItemDecoration.VERTICAL_LIST));
    }

    /**
     * 加载用户数据
     * 曾博晖
     * 2016年8月23日17:25:33
     * 创建
     * */
    private void initData() {
        data = new ArrayList<>();
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
        data.add(contect1);
        data.add(contect2);
        data.add(contect3);
    }

    private void initView(View view){
        rvCollectCards=(RecyclerView)view.findViewById(R.id.rv_collect_cards);
    }
}
