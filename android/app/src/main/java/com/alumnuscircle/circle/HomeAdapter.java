package com.alumnuscircle.circle;

import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import com.alumnuscircle.R;

import java.util.List;

/**
 * Created by 15359 on 2016/8/23.
 */
public class HomeAdapter extends RecyclerView.Adapter<HomeAdapter.HomeHolder> {
    private List<String> names;//对应模块的标题
    private List<Integer>images;//对应模块的图片
    private OnItemClickListener onItemClickListener;

    public HomeAdapter(List<String> names, List<Integer> images)
    {
        this.names = names;
        this.images = images;
        //增加创建圈子
        names.add("创建圈子");
        images.add(R.mipmap.add);
    }

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
    //增加圈子
    public void addItem(String title, int image)
    {
        //插入的位置
        int insertPosition = images.size()-1;
        names.add(insertPosition,title);
        images.add(insertPosition,image);
        notifyItemInserted(insertPosition);
    }
//删除圈子
    public void removeItem(int position)
    {
        names.remove(position);
        images.remove(position);
        notifyItemRemoved(position);
    }

    @Override
    public HomeAdapter.HomeHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        //加载每一项的视图
        View itemView = LayoutInflater.from(parent.getContext()).inflate(R.layout.home_adapter,parent,false);
        HomeHolder homeHolder =new HomeHolder(itemView,onItemClickListener);
        return homeHolder;
    }

    @Override
    public void onBindViewHolder(HomeAdapter.HomeHolder holder, int position) {
        holder.textView.setText(names.get(position));
        holder.imageView.setBackgroundResource(images.get(position));
    }

    @Override
    public int getItemCount() {
        return (images == null)?0:images.size();
    }

    public class HomeHolder extends RecyclerView.ViewHolder implements View.OnClickListener{
        private ImageView imageView;
        private TextView textView;
        private OnItemClickListener onItemClickListener;
        public HomeHolder(View itemView,OnItemClickListener onItemClick) {
            super(itemView);
            imageView = (ImageView)itemView.findViewById(R.id.homeImg);
            textView = (TextView)itemView.findViewById(R.id.homeTv);
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
