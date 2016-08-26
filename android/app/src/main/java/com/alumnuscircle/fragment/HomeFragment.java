package com.alumnuscircle.fragment;

import android.app.Fragment;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.widget.GridLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;

import com.alumnuscircle.R;
import com.alumnuscircle.circle.CircleAdapter;
import com.alumnuscircle.circle.DividerGridItemDecoration;
import com.alumnuscircle.circle.HomeAdapter;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by 15359 on 2016/8/22.
 */
public class HomeFragment extends Fragment implements HomeAdapter.OnItemClickListener {
    private List<Integer> images;
    private List<String>titles;
    private RecyclerView recyclerView;
    private int lastPosition;//创建圈子的位置
    private  HomeAdapter homeAdapter;
    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_homepage, container, false);
        recyclerView=(RecyclerView)view.findViewById(R.id.homeRv);
        //网格布局
        recyclerView.setLayoutManager(new GridLayoutManager(view.getContext(),2));

        InitList();
       homeAdapter = new HomeAdapter(titles,images);
        recyclerView.setAdapter(homeAdapter);
        homeAdapter.setOnItemClickListener(this);
        return view;
    }
    //初始化列表
    private void InitList()
    {
        images = new ArrayList<>();
        titles = new ArrayList<>();

        images.add(R.mipmap.addr);
        images.add(R.mipmap.back);
        images.add(R.mipmap.dynamic);


        titles.add("一个");
        titles.add("两个");
        titles.add("三个");


        lastPosition = images.size();
    }

    @Override
    public void onItemClick(View v, int position) {
        if(position!=lastPosition) {
          TextView tv =(TextView)v.findViewById(R.id.homeTv);
            Toast.makeText(getActivity(), tv.getText().toString() + position, Toast.LENGTH_SHORT).show();
        }
        else
        {
           homeAdapter.addItem("新的项",R.mipmap.me_pressed);
            lastPosition++;
        }
    }
}
