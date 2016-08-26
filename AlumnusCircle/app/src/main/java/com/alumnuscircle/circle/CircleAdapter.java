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
public class CircleAdapter extends RecyclerView.Adapter<CircleAdapter.CircleHolder> {
    private List<String>names;//对应模块的标题
    private List<Integer>images;//对应模块的图片
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
    public CircleAdapter(List<String> names, List<Integer> images)
    {
        this.images = images;
        this.names = names;
    }
    @Override
    public CircleAdapter.CircleHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        //加载每一项的视图
        View itemView = LayoutInflater.from(parent.getContext()).inflate(R.layout.circle_adapter,parent,false);
       CircleHolder circleHolder = new CircleHolder(itemView,onItemClickListener);
        return circleHolder;
    }

    @Override
    public void onBindViewHolder(CircleAdapter.CircleHolder holder, int position) {
        holder.textView.setText(names.get(position));
        holder.imageView.setBackgroundResource(images.get(position));
    }

    @Override
    public int getItemCount() {
        return names.size();
    }


     class CircleHolder extends RecyclerView.ViewHolder implements View.OnClickListener {

         private ImageView imageView;
         private TextView textView;
         private OnItemClickListener onItemClickListener;
         protected CircleHolder(View itemView,OnItemClickListener onItemClick) {
             super(itemView);
             imageView = (ImageView)itemView.findViewById(R.id.circleImg);
             textView = (TextView)itemView.findViewById(R.id.circleTv);
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
