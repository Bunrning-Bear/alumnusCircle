package com.alumnuscircle.circleDetail;

import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.alumnuscircle.R;

/**
 * 个人详情的适配器
 * Created by 白洋 on 2016/8/26.
 */
public class DetailAdapter extends RecyclerView.Adapter<DetailAdapter.DetailHolder> {

   private OnItemClickListener onItemClickListener;
    //点击事件的接口
    public interface OnItemClickListener
    {
        void onItemClick(View v,int position);//实现的方法
    }

    //设置点击事件的接口
    public void setOnItemClickListener(OnItemClickListener onItemClickListener)
    {
        if(onItemClickListener!=null)
            this.onItemClickListener = onItemClickListener;
    }
    @Override
    public DetailAdapter.DetailHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.detail_adapter,parent,false);
        DetailHolder detailHolder = new DetailHolder(view,onItemClickListener);
        return detailHolder;
    }

    @Override
    public void onBindViewHolder(DetailAdapter.DetailHolder holder, int position) {

    }

    @Override
    public int getItemCount() {
        return 0;
    }

    public class DetailHolder extends RecyclerView.ViewHolder implements View.OnClickListener {
        private OnItemClickListener onItemClickListener;
        public DetailHolder(View itemView,OnItemClickListener onItemClick) {
            super(itemView);
            this.onItemClickListener = onItemClick;
            itemView.setOnClickListener(this);
        }

        @Override
        public void onClick(View v) {
            if(onItemClickListener!=null)
                onItemClickListener.onItemClick(v,getPosition());
        }
    }
}
