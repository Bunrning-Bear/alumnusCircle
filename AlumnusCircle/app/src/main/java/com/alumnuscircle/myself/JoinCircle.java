package com.alumnuscircle.myself;

import android.app.Fragment;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.alumnuscircle.R;
import com.alumnuscircle.connections.Adapter.ContactsAdapter;
import com.alumnuscircle.connections.Item.ContactsItem;
import com.alumnuscircle.myself.rvcircle.CircleAdapter;
import com.alumnuscircle.myself.rvcircle.CircleItem;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by chine on 2016/8/26.
 */
public class JoinCircle extends Fragment {

    private View view;
    private LayoutInflater layoutInflater;
    private ViewGroup container;

    private RecyclerView rvJoinCircle;
    private List<CircleItem> data;
    private CircleAdapter adapter;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        view = inflater.inflate(R.layout.me_join_circle, container, false);
        layoutInflater = inflater;
        this.container = container;
        initView(view);
        initData();
        initRecycleView();
        return view;
    }

    private void initRecycleView() {
        rvJoinCircle.setLayoutManager(new LinearLayoutManager(getActivity()));
        rvJoinCircle.setAdapter(adapter = new CircleAdapter(getActivity(), data));

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
        CircleItem item1=new CircleItem(
                "http://img2.imgtn.bdimg.com/it/u=3413454958,4293050372&fm=11&gp=0.jpg",
                "软件圈"
        );
        CircleItem item2=new CircleItem(
                "http://img2.imgtn.bdimg.com/it/u=3413454958,4293050372&fm=11&gp=0.jpg",
                "软件圈"
        );
        CircleItem item3=new CircleItem(
                "http://img2.imgtn.bdimg.com/it/u=3413454958,4293050372&fm=11&gp=0.jpg",
                "软件圈"
        );

        data.add(item1);
        data.add(item2);
        data.add(item3);
    }

    private void initView(View view){
        rvJoinCircle=(RecyclerView)view.findViewById(R.id.rv_join_circle);
    }

}
